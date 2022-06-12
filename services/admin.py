from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from .models import ServiceSchedule
from .models import ServiceTicket

# Register your models here.
admin.site.register(ServiceSchedule)


@admin.register(ServiceTicket)
class ServiceTicketAdmin(admin.ModelAdmin):
    """Admin View for Service Ticket"""

    list_display = (
        'title',
        'cost',
        'date',
        'approval_status',
        'view_vehicles_link',

    )
    list_filter = (
        'title',
        'cost',
        'approval_status',
    )
    fields = ("ref_no", "title", "driver", "vehicle", "approval_status", "item_serviced", "frequency", "cost", "date")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['approval_status'].disabled = True

        return form

    def view_vehicles_link(self, obj):
        count = obj.vehicle.count('make')
        #count = obj.person_set.count()
        url = (
                reverse("admin:vehicles_vehicle_changelist")
                + "?"
                + urlencode({"servicetickets__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Vehicles</a>', url, count)

    view_vehicles_link.short_description = "Vehicles"
