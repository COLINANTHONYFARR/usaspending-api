# Generated by Django 3.2.13 on 2022-08-26 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0001_create_schemas'),
        ('search', '0012_removing_subaward_models'),
    ]

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE IF EXISTS public.subaward_search SET SCHEMA rpt;",
            reverse_sql="ALTER TABLE IF EXISTS rpt.subaward_search SET SCHEMA public;"
        ),
        migrations.RunSQL(
            sql="ALTER TABLE IF EXISTS public.award_search SET SCHEMA rpt;",
            reverse_sql="ALTER TABLE IF EXISTS rpt.award_search SET SCHEMA public;"
        ),
    ]