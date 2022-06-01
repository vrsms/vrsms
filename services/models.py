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
    frequency = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    date = models.DateTimeField()

    class Meta:
        """Meta definition for Service Ticket."""

        verbose_name = 'Service Ticket'
        verbose_name_plural = 'Service Tickets'

        permissions = [
            ("change_service_ticket_status", "Can change the status of service tickets"),
            ("close_service_ticket", "Can remove a service ticket by setting its status as closed"),
        ]

    def __str__(self):
        return self.title


class ServiceSchedule(models.Model):
    ref = models.CharField(_('Reference'), max_length=30)
