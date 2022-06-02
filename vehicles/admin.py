# vehicles/admin.py
# ==============

from django.contrib import admin

from services.models import ServiceTicket
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """Admin View for Vehicle"""

    list_display = (
        'plate_number',
        'category',
        'status',
        'total_service_cost',
    )
    list_filter = (
        'category',
        'make',
        'status',
    )

    def total_service_cost(self, obj):
        from django.db.models import Sum
        result = ServiceTicket.objects.filter(vehicle=obj).aggregate(Sum("cost"))
        return result["cost__sum"]
