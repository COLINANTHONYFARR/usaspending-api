# Generated by Django 2.2.27 on 2022-03-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0090_add_back_faba_covid_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='brokersubaward',
            name='awardee_or_recipient_uei',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='brokersubaward',
            name='sub_awardee_or_recipient_uei',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='brokersubaward',
            name='sub_ultimate_parent_uei',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='brokersubaward',
            name='ultimate_parent_uei',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subaward',
            name='parent_recipient_uei',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subaward',
            name='recipient_uei',
            field=models.TextField(blank=True, null=True),
        ),
    ]