# urls.py (add to the existing urls.py)
from django.urls import path
from .views import salary_report

urlpatterns = [
    path('salary-report/', salary_report, name='salary_report'),
]
