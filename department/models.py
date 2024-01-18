from django.db import models

# Create your models here.
# models.py (add to the existing models.py)
class Department(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()

    def __str__(self):
        return self.name