from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Vehicle(models.Model):
    """Model definition for Vehicle."""

    plate_number = models.CharField(_('Plate Number'), max_length=30)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(_("Make"), max_length=30)
    model = models.CharField(_('Vehicle Model'), max_length=30)
    category = models.CharField(_("Category"), max_length=30)
    status = models.CharField(_('Operation status'), max_length=30)

    class Meta:
        """Meta definition for Vehicle."""

        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

        ordering = ("plate_number", "driver", "make", "model", "category", "status")

    def __str__(self):
        """Unicode's representation of Vehicle."""

        return self.plate_number
