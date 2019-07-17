from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# dojo/views.py


def mysum(request, numbers):
    numbers=sum(map(lambda s: int(s or 0), numbers.split('/')))
    return HttpResponse(numbers)