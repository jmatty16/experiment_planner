# Generated by Django 3.0.2 on 2020-02-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocols', '0002_auto_20200125_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='days_between',
            field=models.IntegerField(default=1),
        ),
    ]