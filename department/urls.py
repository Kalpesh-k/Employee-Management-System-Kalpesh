# urls.py (add to the existing urls.py)
from django.urls import path
from .views import department_list, department_hierarchy

urlpatterns = [
    path('', department_list, name='department_list'),
    path('departments/<int:department_id>/hierarchy/', department_hierarchy, name='department_hierarchy'),
]
