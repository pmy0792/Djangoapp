from lib2to3.refactor import MultiprocessingUnsupported
from pydoc_data.topics import topics
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect
from django.urls import reverse
from django.http import Http404

from .models import *

question_num=Question.objects.all().count()

def index(request):
    question_list=Question.objects.all()
    context={'question_list':question_list}
    return render(request,'firstapp/index.html',context)
    
def test(request):
    question=get_object_or_404(Question,pk=1)
    user_ip=request.META['REMOTE_ADDR']
    
    if not User.objects.filter(user_ip=user_ip).exists():
        u=User(user_ip=request.META['REMOTE_ADDR'])
        u.save()
        
    user_obj=User.objects.get(user_ip=user_ip)
        
    if request.method=="GET":
        return render(request,'firstapp/test.html',{'question': question})
    
    elif request.method=="POST":
        print(request.POST['choice'])
        # 1) 선택지 Voting 모델에 저장
        selected_choice=get_object_or_404(Choice,pk=request.POST['choice'])
        selected_choice.votes+=1
        selected_choice.save()
        
        vote=Voting(user_ip=user_obj, question=question,choice=selected_choice)
        vote.save()
        
        # 2-1) 해당 질문이 마지막 질문일 경우 결과 페이지로 render
        if question_num==int(request.POST['question_id']):
            # 해당 user의 최근 투표 데이터 가져와서 결과 산출
            votings=Voting.objects.filter(user_ip__user_ip=user_ip).values('choice')
            print(votings)
            
            result=1
            context={'result_type':result}
            return render(request,'firstapp/result.html',context)
        
        # 2-2) 그다음 질문 내용 가져와서 render
        else:
            next_question_id= int(request.POST['question_id']) + 1
            question=get_object_or_404(Question,pk=next_question_id)
            return render(request,'firstapp/test.html',{'question': question})
            #return HttpResponseRedirect(reverse('firstapp:test',args=(question,)))
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