from django.contrib import admin
from .models import Suggestion


# Register your models here.


@admin.register(Suggestion)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Suggestion"""

    list_display = (
        'title',
        'is_publishable',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_publishable',
        'created_at',
        'updated_at',
    )
