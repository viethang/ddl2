from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    sciper = models.CharField(max_length=4)

class Result(models.Model):
    gpa = models.FloatField()
    student = models.OneToOneField(Student)