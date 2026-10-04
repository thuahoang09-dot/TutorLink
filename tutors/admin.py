from django.contrib import admin
from .models import Subject, TutorProfile

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order', 'slug', 'icon')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(TutorProfile)
class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'price_per_hour', 'location', 'teaching_method', 'approval_status')
    list_filter = ('approval_status', 'teaching_method')
    search_fields = ('user__username', 'location')
