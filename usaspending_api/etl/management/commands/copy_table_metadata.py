import logging
import re
import asyncio
from django import db
from django.core.management.base import BaseCommand

from usaspending_api.common.data_connectors.async_sql_query import async_run_creates
from usaspending_api.common.helpers.timing_helpers import ConsoleTimer as Timer
from usaspending_api.etl.broker_etl_helpers import dictfetchall

logger = logging.getLogger("script")

# copied from usaspending_api/database_scripts/matview_generator/shared_sql_generator.py
# since that script uses relative imports which do not work well with the rest of the repo code
TEMPLATE = {
    "read_indexes": "SELECT indexname, indexdef FROM pg_indexes WHERE schemaname = '{}' AND tablename = '{}';",
    "read_constraints": "select conname, pg_get_constraintdef(oid) from pg_constraint where contype IN ('p', 'f', 'u') and conrelid = '{}'::regclass;",
}


def make_read_indexes(table_name):
    if "." in table_name:
        schema_name, table_name = table_name[: table_name.index(".")], table_name[table_name.index(".") + 1 :]
    else:
        schema_name = "public"

    return [TEMPLATE["read_indexes"].format(schema_name, table_name)]


def make_read_constraints(table_name):
    return [TEMPLATE["read_constraints"].format(table_name)]


def create_indexes(index_definitions, index_concurrency):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(index_with_concurrency(index_definitions, index_concurrency))
    loop.close()


async def index_with_concurrency(index_definitions, index_concurrency):
    semaphore = asyncio.Semaphore(index_concurrency)
    tasks = []

    async def create_with_sem(sql, index):
        async with semaphore:
            return await async_run_creates(
                sql,
                wrapper=Timer(f"Creating Index {index}"),
            )

    for i, sql in enumerate(index_definitions):
        logger.info(f"Creating future for index: {i} - SQL: {sql}")
        tasks.append(create_with_sem(sql, i))

    return await asyncio.gather(*tasks)


def make_copy_constraints(
    cursor,
    source_table,
    dest_table,
    drop_foreign_keys=False,
    source_suffix="",
    dest_suffix="temp",
    only_parent_partitioned_table=False,
):
    # read the existing indexes
    cursor.execute(make_read_constraints(source_table)[0])
    src_constrs = dictfetchall(cursor)

    # build the destination index sql
    dest_constr_sql = []
    for src_constr_dict in src_constrs:
        src_constr_name = src_constr_dict["conname"]
        root_constr_name = src_constr_name[:-len(f"_{source_suffix}")] if source_suffix else src_constr_name
        dest_constr_name = f"{root_constr_name}_{dest_suffix}" if dest_suffix else root_constr_name
        create_constr_content = src_constr_dict["pg_get_constraintdef"]
        if "FOREIGN KEY" in create_constr_content and drop_foreign_keys:
            continue
        only_clause = ""
        if only_parent_partitioned_table:
            only_clause = "ONLY "
        dest_constr_sql.append(
            f"ALTER TABLE {only_clause}{dest_table} ADD CONSTRAINT {dest_constr_name} {create_constr_content}"
        )
    return dest_constr_sql


def make_copy_indexes(
    cursor, source_table, dest_table, source_suffix="", dest_suffix="temp", only_parent_partitioned_table=False
):
    # read the existing indexes of source table
    cursor.execute(make_read_indexes(source_table)[0])
    src_indexes = dictfetchall(cursor)

    # reading the existing indexes of destination table (to not duplicate anything)
    cursor.execute(make_read_indexes(dest_table)[0])
    dest_indexes = [ix_dict["indexname"] for ix_dict in dictfetchall(cursor)]

    # build the destination index sql
    dest_ix_sql = []
    for src_ix_dict in src_indexes:
        src_ix_name = src_ix_dict["indexname"]
        root_ix_name = src_ix_name[:-len(f"_{source_suffix}")] if source_suffix else src_ix_name
        dest_ix_name = f"{root_ix_name}_{dest_suffix}" if dest_suffix else root_ix_name
        if dest_ix_name in dest_indexes:
            logger.info(f"Index {dest_ix_name} already in {dest_table}. Skipping.")
            continue

        only_clause = ""
        if only_parent_partitioned_table:
            only_clause = "ONLY "

        create_ix_sql = src_ix_dict["indexdef"]

        # (?:ONLY\s+)? is an optional word (ONLY) in a non-capturing group
        # this regex *should* match source_table, but can get funky with/without the schema included and regex
        # for example, a table 'x' in the public schema could be provided and the string will include `public.x'
        ix_regex = rf"CREATE\s+.*INDEX\s+\S+\s+ON\s+(?:ONLY\s+)?(\S+)\s+.*"
        src_table = re.findall(ix_regex, create_ix_sql)[0]

        create_ix_sql = create_ix_sql.replace(src_ix_name, dest_ix_name)
        create_ix_sql = create_ix_sql.replace(src_table, f"{only_clause}{dest_table}")
        dest_ix_sql.append(create_ix_sql)
    return dest_ix_sql


class Command(BaseCommand):

    help = """
    This command simply copies the constraints and indexes from one table to another in postgres
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--source-table",
            type=str,
            required=True,
            help="The source postgres table to read the metadata",
        )
        parser.add_argument(
            "--source-suffix",
            type=str,
            required=False,
            nargs="?",
            const="",  # value if flag provided but no arg values given
            default="",
            help="The assumed suffix on the source table name and all objects (like index names) of the source table",
        )
        parser.add_argument(
            "--dest-table",
            type=str,
            required=True,
            help="The destination postgres table to copy the metadata to",
        )
        parser.add_argument(
            "--dest-suffix",
            type=str,
            required=False,
            nargs="?",
            const="",  # value if flag provided but no arg values given
            default="temp",
            help="The assumed suffix on the destination table name and all objects (like index names) of the "
            "destination table",
        )
        parser.add_argument(
            "--keep-foreign-constraints",
            action="store_true",
            help="If provided, copies over the foreign constraints to the destination table.",
        )
        parser.add_argument(
            "--skip-constraints",
            action="store_true",
            help="If provided, skips copying over the constraints to the destination table.",
        )
        parser.add_argument(
            "--skip-indexes",
            action="store_true",
            help="If provided, skips copying over the indexes to the destination table.",
        )
        parser.add_argument(
            "--max-parallel-maintenance-workers",
            type=int,
            required=False,
            help="Postgres session setting for max parallel workers for creating indexes.",
        )
        parser.add_argument(
            "--maintenance-work-mem",
            type=int,
            required=False,
            help="Postgres session setting for max memory to use for creating indexes (in GBs).",
        )
        parser.add_argument(
            "--index-concurrency",
            type=int,
            default=5,
            help="Concurrency limit for index creation.",
        )
        parser.add_argument(
            "--only-parent-partitioned-table",
            action="store_true",
            help="If this flag is provided, it is instructing the use of the 'ONLY' keyword when applying INDEXes or "
            "CONSTRAINTs to a parent partitioned table (only).",
        )

    def handle(self, *args, **options):
        # Resolve Parameters
        source_table = options["source_table"]
        source_suffix = options["source_suffix"]
        dest_table = options["dest_table"]
        dest_suffix = options["dest_suffix"]
        keep_foreign_constraints = options["keep_foreign_constraints"]
        skip_constraints = options["skip_constraints"]
        skip_indexes = options["skip_indexes"]
        max_parallel_maintenance_workers = options["max_parallel_maintenance_workers"]
        maintenance_work_mem = options["maintenance_work_mem"]
        index_concurrency = options["index_concurrency"]
        only_parent_partitioned_table = options["only_parent_partitioned_table"]

        logger.info(f"Copying metadata from table {source_table} to table {dest_table}.")

        copy_index_sql = None
        with db.connection.cursor() as cursor:
            if not skip_constraints:
                logger.info(f"Copying constraints over from {source_table}")
                copy_constraint_sql = make_copy_constraints(
                    cursor,
                    source_table,
                    dest_table,
                    drop_foreign_keys=not keep_foreign_constraints,
                    source_suffix=source_suffix,
                    dest_suffix=dest_suffix,
                    only_parent_partitioned_table=only_parent_partitioned_table,
                )
                if copy_constraint_sql:
                    cursor.execute("; ".join(copy_constraint_sql))
                logger.info(f"Constraints from {source_table} copied over")

            if not skip_indexes:
                # Ensuring we're using the max cores available when generating indexes
                if max_parallel_maintenance_workers:
                    logger.info(f"Setting max_parallel_maintenance_workers to {max_parallel_maintenance_workers}")
                    cursor.execute(f"SET max_parallel_maintenance_workers = {max_parallel_maintenance_workers}")
                if maintenance_work_mem:
                    logger.info(f"Setting maintenance_work_mem to '{maintenance_work_mem}GB'")
                    cursor.execute(f"SET maintenance_work_mem = '{maintenance_work_mem}GB'")
                copy_index_sql = make_copy_indexes(
                    cursor,
                    source_table,
                    dest_table,
                    source_suffix=source_suffix,
                    dest_suffix=dest_suffix,
                    only_parent_partitioned_table=only_parent_partitioned_table,
                )
        if copy_index_sql:
            logger.info(f"Copying indexes over from {source_table}.")
            create_indexes(copy_index_sql, index_concurrency)
            logger.info(f"Indexes from {source_table} copied over.")
