from django.db import models

# Create your models here.


class Student(models.Model):
    PROGRAMS = (
        ('certificate', 'Certificate'),
        ('diploma', 'Diploma'),
        ('degree', 'Degree'),
    )
    picture = models.ImageField(upload_to="images/students", blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    other_names = models.CharField(max_length=150, blank=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)
    program = models.CharField(max_length=11, choices=PROGRAMS)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
