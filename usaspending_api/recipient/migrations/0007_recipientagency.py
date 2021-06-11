# Generated by Django 2.2.17 on 2021-05-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipient', '0006_auto_20210315_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipientAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fiscal_year', models.IntegerField(db_index=True)),
                ('toptier_code', models.TextField(db_index=True)),
                ('recipient_hash', models.UUIDField(db_index=True)),
                ('recipient_name', models.TextField(null=True)),
                ('recipient_amount', models.DecimalField(decimal_places=2, max_digits=23)),
            ],
            options={
                'db_table': 'recipient_agency',
                'managed': True,
            },
        ),
    ]
