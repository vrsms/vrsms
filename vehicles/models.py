from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Vehicle(models.Model):
    """Model definition for Vehicle."""

    make = models.CharField(_("Make"), max_length=30)
    model = models.CharField('vehicle_model', max_length=30)
    plate_number = models.CharField('Plate number', max_length=30)
    category = models.CharField(max_length=30)
    status = models.CharField('Operation status', max_length=30)

    class Meta:
        """Meta definition for Vehicle."""

        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        """Unicode's representation of Vehicle."""
        return self.plate_number
