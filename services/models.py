from __future__ import unicode_literals
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from vehicles.models import Vehicle


# Create your models here.


class ServiceTicket(models.Model):
    """Model definition for Service Ticket."""

    driver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ref_no = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=50, editable=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=30)
    approval_status = models.BooleanField(_('Is It Approved ?'), default=False)
    item_serviced = models.CharField(max_length=30)
    frequency = models.PositiveBigIntegerField(default=0)
    cost = models.PositiveBigIntegerField(default=0)
    date = models.DateTimeField()

    class Meta:
        """Meta definition for Service Ticket."""

        verbose_name = 'Service Ticket'
        verbose_name_plural = 'Service Tickets'

        permissions = [
            ("change_service_ticket_status", "Can change the status of service tickets"),
            ("close_service_ticket", "Can remove a service ticket by setting its status as closed"),
        ]

        ordering = ("ref_no", "title", "driver", "vehicle", "approval_status", "item_serviced", "frequency", "cost",
                    "date")

    def __str__(self):
        return self.title


class ServiceSchedule(models.Model):
    CHOICES = (
        ("30000", "30k"),
        ("60000", "60k"),
        ("90000", "90k"),
        )
    schedule_name = models.CharField(_('Schedule Name'), max_length=100)
    ref_no = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=50, editable=True)
    service_mark = models.CharField(max_length=250, null=False, choices=CHOICES)

    def __str__(self):
        return self.schedule_name

    class Meta:
        """Meta definition for Service Schedule."""

        verbose_name = 'Service Schedule'
        verbose_name_plural = 'Service Schedules'

