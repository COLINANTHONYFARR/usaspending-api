import logging
import signal

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db import transaction
from usaspending_api.submissions.models import SubmissionAttributes


class Command(BaseCommand):
    """
    This command will remove a submission and all associated data with it from the
    database
    """

    help = "Removes a single submission from the configured data broker database"
    logger = logging.getLogger("console")

    def add_arguments(self, parser):
        parser.add_argument("submission_id", help="the broker submission id to delete", type=int)

    @transaction.atomic
    def handle(self, *args, **options):
        self.logger.info("Starting rm_submissions management command")

        def signal_handler(signal, frame):
            transaction.set_rollback(True)
            raise Exception("Received interrupt signal. Aborting...")

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        submission_id = options["submission_id"]

        try:
            submission = SubmissionAttributes.objects.get(submission_id=submission_id)
        except ObjectDoesNotExist:
            raise RuntimeError(f"Broker submission id {submission_id} does not exist")

        deleted_stats = submission.delete()

        self.logger.info("Finished deletions.")

        statistics = f"Statistics:\n  Total objects removed: {deleted_stats[0]:,}"
        for (model, count) in deleted_stats[1].items():
            statistics += f"\n  {model}: {count:,}"

        self.logger.info(f"Deleted broker submission id {submission_id}. {statistics}")
