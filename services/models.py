from django.db import models
from vehicles.models import Vehicle
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class ServiceTicket(models.Model):
    """Model definition for Service Ticket."""

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
