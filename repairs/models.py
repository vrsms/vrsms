from django.db import models
from vehicles.models import Vehicle
from django.utils.translation import ugettext_lazy as _
from . import Ticket


# Create your models here.
class RepairTicket(Ticket.Ticket):
    """Model definition for Repair Ticket."""

    super(Ticket.Ticket)
    frequency = models.IntegerField(_('frequency'), default=0)

    class Meta:
        """Meta definition for Repair Ticket."""

        verbose_name = 'Repair Ticket'
        verbose_name_plural = 'Repair Tickets'

        ordering = ("title", "ref_no", "driver", "vehicle", "approval_status", "item_maintained", "frequency", "cost",
                    "date")

    def __str__(self):
        return self.title
