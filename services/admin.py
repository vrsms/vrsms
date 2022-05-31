from django.contrib import admin
from .models import Vehicle
from .models import ServiceTicket
from .models import ServiceSchedule

# Register your models here.
admin.site.register(ServiceSchedule)


@admin.register(ServiceTicket)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Service Ticket"""

    list_display = (
        'title',
        'cost',
        'date',
        'status',
    )
    list_filter = (
        'title',
        'cost',
        'status',
    )
