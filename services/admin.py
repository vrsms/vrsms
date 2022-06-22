from django.contrib import admin
from .models import ServiceSchedule
from .models import ServiceTicket
import mawio

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

    def save_model(self, request, obj, form, change):
        # obj.added_by = request.user
        mawio.notify()
        super().save_model(request, obj, form, change)
