# views.py
from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
# employee/views.py

from django.shortcuts import render
from .models import Employee, Department

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})
