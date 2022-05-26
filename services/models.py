from django.db import models
from vehicles.models import Vehicle
from django.utils.translation import ugettext_lazy as _
import uuid


# Create your models here.


class ServiceTicket(models.Model):
    """Model definition for Service Ticket."""
    # ref_no = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=True)
    ref_no = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=50, editable=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=30)
    status = models.CharField(_('Operation status'), max_length=30)
    item_serviced = models.CharField(max_length=30)
    frequency = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    date = models.DateTimeField()

    class Meta:
        """Meta definition for Service Ticket."""

        verbose_name = 'Service Ticket'
        verbose_name_plural = 'Service Tickets'

    def __str__(self):
        return self.title


class ServiceSchedule(models.Model):
    ref = models.CharField(_('Reference'), max_length=30)
