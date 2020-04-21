# Generated by Django 3.0.2 on 2020-03-07 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocols', '0009_event_minutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='step',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='protocols.Step'),
            preserve_default=False,
        ),
    ]