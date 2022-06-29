from django.contrib.auth import get_user_model
from django.db import models
from vehicles.models import Vehicle
from django.utils.translation import ugettext_lazy as _
import uuid


class Ticket(models.Model):
    """Model definition for Ticket."""

    Repairs = (
        ("1", "30k"),
        ("2", "60k"),
        ("3", "90k"),
    )

    ref_no = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=50, editable=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(_('Repair Title'), max_length=100)
    item_maintained = models.CharField(max_length=30)
    cost = models.PositiveBigIntegerField(default=0)
    date = models.DateTimeField()
    approval_status = models.BooleanField(_('Is It Approved ?'), default=False)
    driver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Service Ticket."""

        verbose_name = 'Repair Ticket'
        verbose_name_plural = 'Repair Tickets'
        ordering = ("title", "ref_no", "driver", "vehicle", "approval_status", "item_maintained", "cost", "date")

    def __str__(self):
        return self.title
