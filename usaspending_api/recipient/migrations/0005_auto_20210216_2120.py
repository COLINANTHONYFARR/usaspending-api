# Generated by Django 2.2.9 on 2021-02-16 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipient', '0004_auto_20210216_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipientprofile',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]