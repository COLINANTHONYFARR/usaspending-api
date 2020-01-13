# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-11 00:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipient', '0001_initial'),
    ]

    # For some reason, these indexes were still created and not dropped if I put this command at the
    # bottom of 0001_initial
    operations = [
        migrations.RunSQL(
            sql=[
                'drop index if exists duns_awardee_or_recipient_uniqu_81b7969d_like',
                'drop index if exists recipient_lookup_duns_ae948c75_like',
            ],
        ),
    ]