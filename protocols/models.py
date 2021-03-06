from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from datetime import date, timedelta
from .Protocol import ProtocolLinkedList, RSDStep, SDStep, TDStep


class Protocol(models.Model):
    name = models.CharField(max_length=200)
    days = models.IntegerField(default=1)
    description = models.CharField(max_length=200)
    protocol_ll = ProtocolLinkedList()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE)
    type = models.CharField(max_length=50,
                            choices=[('default', 'default'),
                                     ('SDS', 'SDS'),
                                     ('RSDS', 'RSDS'),
                                     ('TDS', 'TDS')])
    step_text = models.CharField(max_length=1000)
    time_min = models.IntegerField(default=0)
    days_between = models.IntegerField(default=1)
    gap_days = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Feature(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)


class Event(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name="step")
    experiment_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=timezone.now(),)
    minutes = models.IntegerField(default=5)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('protocols:event', args=(self.id,))
        return f'<a href="{url}">{self.title}</a>'


class Experiment(models.Model):
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE)
    earliest_start = models.DateTimeField(default=timezone.now())
    latest_start = models.DateTimeField(default=timezone.now() + timedelta(days=14))
    name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now())
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)





