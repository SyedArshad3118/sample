from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello Viewer : Lets check the working of REST api from SYED ARSHAD')