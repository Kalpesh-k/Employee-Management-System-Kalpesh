from django.contrib import admin

# Register your models here.
# admin.py (add to the existing admin.py)
from .models import EmployeeSalary

@admin.register(EmployeeSalary)
class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'start_date', 'end_date')
