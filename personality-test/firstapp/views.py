from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome") #response by http to client


def result(request, type):
    return HttpResponse("Result: "+type)