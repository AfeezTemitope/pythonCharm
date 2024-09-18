from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'age', 'gender')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('gender',)
