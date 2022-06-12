# vehicles/admin.py
# ==============

from django.contrib import admin
from django.db.models import Sum

from repairs.models import RepairTicket
from services.models import ServiceTicket
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """Admin View for Vehicle"""

    list_display = (
        'plate_number',
        'status',
        'total_repair_cost',
        'total_service_cost',

    )
    list_filter = (
        'category',
        'make',
        'status',
    )

    def total_repair_cost(self, obj: Vehicle):
        """ Calculate the total service cost for each Vehicle object"""

        result = RepairTicket.objects.filter(vehicle=obj).aggregate(Sum("cost"))
        return result["cost__sum"]

    total_repair_cost.short_description = "Total Repair Costs"

    def total_service_cost(self, obj: Vehicle):
        """ Calculate the total service cost for each Vehicle object"""

        result = ServiceTicket.objects.filter(vehicle=obj).aggregate(Sum("cost"))
        return result["cost__sum"]

    total_service_cost.short_description = "Total Service Costs"
