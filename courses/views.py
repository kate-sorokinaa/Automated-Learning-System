from django.shortcuts import render
from .models import Course


def courses_home(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_home.html', {'courses': courses})


def learn(request):
    return render(request, 'courses/learn.html')
