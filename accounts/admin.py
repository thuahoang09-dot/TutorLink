from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'full_name', 'phone', 'is_locked', 'created_at')
    list_filter = ('role', 'is_locked')
    search_fields = ('user__username', 'full_name', 'phone')
