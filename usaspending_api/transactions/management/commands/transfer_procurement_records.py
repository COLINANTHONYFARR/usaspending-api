from django.core.management.base import BaseCommand

from usaspending_api.transactions.agnostic_transaction_loader import AgnosticTransactionLoader
from usaspending_api.transactions.models.source_procurement_transaction import SourceProcurementTransaction


class Command(AgnosticTransactionLoader, BaseCommand):
    help = "Upsert procurement transactions from a Broker database into an USAspending database"
    broker_source_table_name = SourceProcurementTransaction().broker_source_table
    delete_management_command = "delete_procurement_records"
    destination_table_name = SourceProcurementTransaction().table_name
    last_load_record = "source_procurement_transaction"
    lookback_minutes = 0
    shared_pk = "detached_award_procurement_id"
    working_file_prefix = "procurement_load_ids"
    broker_select_sql = 'SELECT "{id}" FROM "{table}" {optional_predicate}'
