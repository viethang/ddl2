from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Student


def details(request, sciper):
    try:
        student = Student.objects.get(pk=sciper)
        res = student.firstname + ' ' + student.lastname + ' -- gpa ' + str(student.gpa())
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'detail.html', {'student': student})

