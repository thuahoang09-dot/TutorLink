from django.contrib import admin
from .models import ClassRequest

@admin.register(ClassRequest)
class ClassRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'subject', 'grade', 'sessions_per_week', 'budget', 'status', 'created_at')
    list_filter = ('status', 'subject', 'teaching_method')
    search_fields = ('title', 'student__username', 'location')
