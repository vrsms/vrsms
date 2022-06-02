# vehicles/admin.py
# ==============

from django.contrib import admin

from repairs.models import RepairTicket
from services.models import ServiceTicket
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """Admin View for Vehicle"""

    list_display = (
        'plate_number',
        'category',
        'status',
        'total_repair_cost',
        'total_service_cost',
    )
    list_filter = (
        'category',
        'make',
        'status',
    )

    def total_repair_cost(self, obj):
        from django.db.models import Sum
        result = RepairTicket.objects.filter(vehicle=obj).aggregate(Sum("cost"))
        return result["cost__sum"]


    def total_service_cost(self, obj):
        from django.db.models import Sum
        result = ServiceTicket.objects.filter(vehicle=obj).aggregate(Sum("cost"))
        return result["cost__sum"]

