# Generated by Django 3.2.15 on 2023-03-02 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0100_ctodlinkageupdates'),
    ]

    operations = [
        migrations.RunSQL(
            sql="DROP TABLE IF EXISTS transaction_fabs",
            reverse_sql="",
        ),
        migrations.RunSQL(
            sql="DROP TABLE IF EXISTS transaction_fpds",
            reverse_sql="",
        ),
        migrations.RunSQL(
            sql="DROP TABLE IF EXISTS transaction_normalized CASCADE",
            reverse_sql="",
        ),
        migrations.RunSQL(
            sql="DROP TABLE IF EXISTS awards",
            reverse_sql="",
        ),
    ]
