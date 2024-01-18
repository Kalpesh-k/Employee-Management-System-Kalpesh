# department/admin.py
from django.contrib import admin
from .models import Department

try:
    admin.site.unregister(Department)
except admin.sites.NotRegistered:
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor')  # Add other fields as needed
