from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Student


def detail(request, sciper):
    try:
        student = Student.objects.get(pk=sciper)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'detail.html', {'student': student})

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

