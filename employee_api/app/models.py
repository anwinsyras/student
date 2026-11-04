from django.db import models


class Employee(models.Model):
    gender_choices = (('male', 'MALE'),('female', 'FEMALE'))

    empid = models.IntegerField()
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=gender_choices)
    salary = models.IntegerField()
    designation = models.CharField(max_length=20)
    joining_date = models.DateField(auto_now_add=True)

# Create your models here.
