from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Course
def index(request):
    courses=Course.objects
    return render(request, 'courses/index.html',{'courses':courses})
