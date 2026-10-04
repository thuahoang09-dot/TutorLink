from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('class_request', 'tutor', 'proposed_price', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('tutor__username', 'class_request__title')
