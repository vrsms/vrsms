from django.db import models
from vehicles.models import Vehicle
from django.utils.translation import ugettext_lazy as _
import uuid


class Ticket(models.Model):
    """Model definition for Ticket."""
    ref_no = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=30)
    item_maintained = models.CharField(max_length=30)
    cost = models.IntegerField(default=0)
    date = models.DateTimeField()
    status = models.CharField(_('Operation status'), max_length=30)

    class Meta:
        """Meta definition for Service Ticket."""

        verbose_name = 'Service Ticket'
        verbose_name_plural = 'Service Tickets'

    def __str__(self):
        return self.title
