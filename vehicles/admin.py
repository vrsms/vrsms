# vehicles/admin.py
# ==============

from django.contrib import admin
from .models import Vehicle


@admin.register(Vehicle)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Vehicle"""

    list_display = (
        'plate_number',
        'model',
        'category',
        'status',
    )
    list_filter = (
        'category',
        'make',
        'status',
    )
