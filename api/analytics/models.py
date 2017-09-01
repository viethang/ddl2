from django.db import models
from functools import reduce


class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    sciper = models.CharField(max_length=4, primary_key=True)

    def gpa(self):
        if len(self.note_set.all()) == 0:
            return 0;

        return reduce((lambda x, y: x.note + y.note), self.note_set.all()) / len(self.note_set.all())

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Note(models.Model):
    subject = models.CharField(max_length=30)
    note = models.FloatField()
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject + ': ' + str(self.note) + ' -- ' + str(self.date)
