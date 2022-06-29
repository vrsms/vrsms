import csv

from django.contrib import admin
import mawio
from .models import RepairTicket
from django.http import HttpResponse, HttpResponseRedirect


# Register your models here.
@admin.register(RepairTicket)
class RepairTicketAdmin(admin.ModelAdmin):
    """Admin View for Repair Ticket"""

    list_display = ('title', 'cost', 'date', 'approval_status',)
    list_filter = ('date', 'approval_status',)
    fields = ("ref_no", "title", "driver", "vehicle", "approval_status", "item_maintained", "frequency", "cost", "date")
    list_per_page = 10
    date_hierarchy = 'date'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['approval_status'].disabled = True

        return form

    def save_model(self, request, obj, form, change):
        """
        Override save button
        Send email to the fleet manager when saving
        """
       # mawio.notify()
        super().save_model(request, obj, form, change)

    actions = ["mark_approved", "export_as_csv", "mark_rejected", ]

    def mark_approved(self, request, queryset):
        self.message_user(request, "Selected repair tickets are now approved")
        queryset.update(approval_status=True)

    mark_approved.short_description = "Approve Selected Repair Tickets"

    def mark_rejected(self, request, queryset):
        self.message_user(request, "Selected repair tickets are now disapproved")
        queryset.update(approval_status=False)

    mark_rejected.short_description = "Reject Selected Repair Tickets"

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)

        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected Service Tickets"

