# vehicles/admin.py
# ==============

from django.contrib import admin
from django.db.models import Sum
from django.urls import reverse, path
from django.utils.html import format_html
from django.utils.http import urlencode
from repairs.models import RepairTicket
from services.models import ServiceTicket
from .models import Vehicle

import io
from django.http import FileResponse, HttpResponseRedirect
from reportlab.pdfgen import canvas


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """Admin View for Vehicle"""

    list_display = (
        'plate_number',
        'status',
        'view_repair_tickets_link',
        'view_service_tickets_link',
        'total_repair_cost',
        'total_service_cost',
        )
    list_filter = ('category', 'make', 'status', )
    change_list_template = "vehicles/vehicles_changelist.html"

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

    def view_repair_tickets_link(self, obj: Vehicle):
        """ Show all repair tickets linked to this vehicle"""

        count = obj.ticket_set.count()

        url = (
                reverse("admin:repairs_repairticket_changelist")
                + "?"
                + urlencode({"repairticket__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Repair Tickets</a>', url, count)

    view_repair_tickets_link.short_description = "Repair Tickets"

    def view_service_tickets_link(self, obj: Vehicle):
        """ Show all service tickets linked to this vehicle"""

        count = obj.serviceticket_set.count()

        url = (
                reverse("admin:services_serviceticket_changelist")
                + "?"
                + urlencode({"serviceticket__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Service Tickets</a>', url, count)

    view_service_tickets_link.short_description = "Service Tickets"
