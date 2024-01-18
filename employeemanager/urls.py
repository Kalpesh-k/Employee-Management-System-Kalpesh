# main_project/urls.py

from django.contrib import admin
from django.urls import path, include
from employee.views import employee_list  # Import a view from one of your apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('department/', include('department.urls')),  # Include department URLs here
    path('salary/', include('salary.urls')),
    path('', include('employee.urls')),  # Assuming you have a home URL pattern in employee.urls
]
