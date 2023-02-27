# Generated by Django 3.2.15 on 2023-02-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0026_award_search_guaid_uq_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='transactionsearch',
            name='ts_idx_award_key_pre2008',
        ),
        migrations.AddIndex(
            model_name='transactionsearch',
            index=models.Index(fields=['generated_unique_award_id'], name='ts_idx_award_key'),
        ),
    ]
