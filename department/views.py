# department/views.py

from django.shortcuts import render
from .models import Department

# department/views.py

from django.shortcuts import render
from .models import Department

# Rest of your views code...

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/templates/department_list.html', {'departments': departments})

def department_hierarchy(request, department_id):
    department = Department.objects.get(pk=department_id)
    return render(request, 'department/templates/department_hierarchy.html', {'department': department})
