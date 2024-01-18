

# salary/models.py
from django.db import models
from employee.models import Employee  # Assuming your Employee model is in the 'employee' app

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salaries')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name}'s salary from {self.start_date} to {self.end_date}"
