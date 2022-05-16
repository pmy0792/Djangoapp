from lib2to3.refactor import MultiprocessingUnsupported
from pydoc_data.topics import topics
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse


def index(request):
    return HttpResponse('This is index page')
    
def result(request, id):
    return HttpResponse("Your looking at the result #"+id)

def statistics(request):
    return HttpResponse("Your looking at the statistic page")