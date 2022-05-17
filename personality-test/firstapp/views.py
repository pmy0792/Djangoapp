from lib2to3.refactor import MultiprocessingUnsupported
from pydoc_data.topics import topics
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect
from django.urls import reverse
#from django.http import Http404

from .models import *

def index(request):
    question_list=Question.objects.all()
    context={'question_list':question_list}
    return render(request,'firstapp/index.html',context)
    
def test(request):
    question=get_object_or_404(Question,pk=1)
    if request.method=="GET":
        return render(request,'firstapp/test.html',{'question': question})
    
    elif request.method=="POST":
        
        next_question_id= request.POST['keyname'] + 1
        question=get_object_or_404(Question,pk=next_question_id)
        return HttpResponseRedirect(reverse('firstapp:test',args=(question,)))
    '''
    try:
        question=Question.objects.get(pk=1)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    '''
    
    
    return render(request,'firstapp/test.html',{'question':question})
    

def result(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary-like object 
        # that lets you access submitted data by key name. 
        # In this case, request.POST['choice'] returns the ID of the selected choice, 
        # as a string. request.POST values are always strings.
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'firstapp/result.html', 
                      {'question':question,
                       'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        
        # reverse() helps avoid having to hardcode a URL in the view function
        return HttpResponseRedirect(reverse('firstapp:result',args=(question.id,)))
    #return HttpResponse("Your looking at the result Question"+question_id)


# It returns an HttpResponse object 
# of the given template rendered with the given context.
def statistics(request):
    return HttpResponse("Your looking at the statistic page")