
from django.urls import path
from .views import employee_list, department_list 

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('departments/', department_list, name='department_list'),  
]
