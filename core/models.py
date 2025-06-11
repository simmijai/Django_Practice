from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)  # ✅ this allows null values

    def __str__(self):
        return self.name