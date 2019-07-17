from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# dojo/views.py


def mysum(request, x):
    return HttpResponse(x)