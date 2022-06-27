from django.contrib import admin
from django.urls import path

from .models import ServiceSchedule
from .models import ServiceTicket
import mawio
from django.http import HttpResponse, HttpResponseRedirect
import csv

# Register your models here.
admin.site.register(ServiceSchedule)


@admin.register(ServiceTicket)
class ServiceTicketAdmin(admin.ModelAdmin):
    """Admin View for Service Ticket"""

    list_display = ('title', 'approval_status', 'date', 'cost',)
    list_filter = ('date', 'approval_status',)
    fields = ("ref_no", "title", "driver", "vehicle", "approval_status", "item_serviced", "frequency", "cost", "date")
    change_list_template = "services/services_changelist.html"
    list_per_page = 250

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

    actions = ["mark_approved", "export_as_csv", "mark_rejected", ]

    def mark_approved(self, request, queryset):
        queryset.update(approval_status=True)

    mark_approved.short_description = "Approve Selected Service Tickets"

    def mark_rejected(self, request, queryset):
        queryset.update(approval_status=False)

    mark_rejected.short_description = "Reject Selected Service Tickets"

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

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('approve/', self.approve),
            path('disapprove/', self.disapprove),
        ]
        return my_urls + urls

    def approve(self, request):
        self.model.objects.all().update(approval_status=True)
        self.message_user(request, "All services tickets are now approved")
        return HttpResponseRedirect("../")

    def disapprove(self, request):
        self.model.objects.all().update(approval_status=False)
        self.message_user(request, "All services tickets are now disapproved")
        return HttpResponseRedirect("../")



