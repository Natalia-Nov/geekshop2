# Generated by Django 2.2.17 on 2021-01-15 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210115_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 17, 12, 14, 47, 902961, tzinfo=utc)),
        ),
    ]