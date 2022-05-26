import random
import string
from django.db import models
from services.models import Vehicle
from django.utils.translation import ugettext_lazy as _
from . import Ticket

# Create your models here.
reference_string = string.ascii_letters + string.digits + string.punctuation


class RepairTicket(Ticket.Ticket):
    """Model definition for Service Ticket."""
    super(Ticket.Ticket)
    # ref = models.CharField('Reference', default=''.join(random.sample(reference_string, 10)), max_length=50)
    #item_maintained = models.CharField(max_length=30)
    frequency = models.IntegerField(default=0)
    super(Ticket.Ticket)

    class Meta:
        """Meta definition for Service Ticket."""

        verbose_name = 'Repair Ticket'
        verbose_name_plural = 'Repair Tickets'

    def __str__(self):
        return self.frequency
