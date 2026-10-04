from django.contrib import admin
from .models import MatchedClass

@admin.register(MatchedClass)
class MatchedClassAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'tutor', 'hourly_rate', 'status', 'start_date')
    list_filter = ('status', 'subject')
    search_fields = ('student__username', 'tutor__username')
