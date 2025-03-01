from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"
