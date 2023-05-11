# Generated by Django 3.2.15 on 2023-03-06 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0028_transaction_search_agency_indexes"),
    ]

    operations = [
        # The latest_transaction_id field already exists, we're just telling Django to link it to the
        # TransactionSearch model (i.e. No DB operations need to be done, just model state operations)
        migrations.RunSQL(
            sql="",
            reverse_sql="",
            state_operations=[
                migrations.RemoveField(
                    model_name="subawardsearch",
                    name="latest_transaction_id",
                ),
                migrations.AddField(
                    model_name="subawardsearch",
                    name="latest_transaction",
                    field=models.ForeignKey(
                        db_constraint=False,
                        help_text="The latest transaction for the prime award by action_date and " "mod",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="subawardsearch",
                        to="search.transactionsearch",
                    ),
                ),
            ],
        )
    ]