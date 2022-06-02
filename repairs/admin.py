from django.contrib import admin
from .models import Vehicle
from .models import RepairTicket


# Register your models here.
@admin.register(RepairTicket)
class RepairTicketAdmin(admin.ModelAdmin):
    """Admin View for Repair Ticket"""

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
    fields = ("ref_no", "title", "driver", "vehicle", "approval_status", "item_maintained", "frequency", "cost", "date")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['approval_status'].disabled = True

        return form
