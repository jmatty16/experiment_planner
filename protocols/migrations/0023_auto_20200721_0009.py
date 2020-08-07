# Generated by Django 3.0.2 on 2020-07-21 05:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('protocols', '0022_auto_20200720_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 5, 9, 14, 342858, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 5, 9, 14, 343855, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='earliest_start',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 5, 9, 14, 343855, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='latest_start',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 4, 5, 9, 14, 343855, tzinfo=utc)),
        ),
    ]
