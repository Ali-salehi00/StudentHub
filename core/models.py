from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    major = models.CharField(max_length=255)
    student_number = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return f"{self.fname}{self.lname}"
    
    