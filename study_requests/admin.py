from django.contrib import admin
from .models import StudyRequest

@admin.register(StudyRequest)
class StudyRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'tutor', 'subject', 'sessions_per_week', 'location', 'status', 'created_at')
    list_filter = ('status', 'subject')
    search_fields = ('student__username', 'tutor__username')
