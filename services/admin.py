from django.contrib import admin

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

    def show_average(self, obj):
        from django.db.models import Avg
        result = ServiceTicket.objects.filter(person=obj).aggregate(Avg("grade"))
        return result["grade__avg"]
