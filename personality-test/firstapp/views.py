from lib2to3.refactor import MultiprocessingUnsupported
from pydoc_data.topics import topics
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect
from django.urls import reverse
from django.http import Http404

from .models import *
from firstapp.ComputeResult import *

question_num=Question.objects.all().count()


def index(request):
    question_list=Question.objects.all()
    context={'question_list':question_list}
    return render(request,'firstapp/index.html',context)
    
def test(request):
    global answering_count
    
    #get_object_or_404(Question,pk=1)
    user_ip=request.META['REMOTE_ADDR']
    
    # 처음 접속하는 유저일 경우 유저 정보 저장
    if not User.objects.filter(user_ip=user_ip).exists():
        u=User(user_ip=request.META['REMOTE_ADDR'])
        u.save()
        
    user_obj=User.objects.get(user_ip=user_ip)
        
    if request.method=="GET":
        answering_count=0
        question=Question.objects.first()
        return render(request,'firstapp/test.html',{'question': question})
    
    elif request.method=="POST":
        answering_count+=1
        #print(request.POST['choice'])
        # 1) 선택지 Voting 모델에 저장
        question=get_object_or_404(Question,pk=request.POST['question_id'])
        selected_choice=get_object_or_404(Choice,pk=request.POST['choice'])
        selected_choice.votes+=1
        selected_choice.save()
        
        vote=Voting(user_ip=user_obj, question=question,choice=selected_choice)
        vote.save()
        
        # 2-1) 해당 질문이 마지막 질문일 경우, 결과 모델에 저장하고 결과 페이지로 render
        if question_num==answering_count:
            # 해당 user의 최근 투표 데이터 가져와서 결과 산출            
            # calculate user result here...
            result=calc_result(user_ip)
            u=UserResultStorage(user_ip=user_obj,type=result)
            u.save()
            result_id=result.id
            
            return HttpResponseRedirect(reverse('firstapp:result',args=(result_id,)))
            return render(request,'firstapp/result.html',context)
        
        # 2-2) 그다음 질문 내용 가져와서 render
        else:
            next_question_id= int(request.POST['question_id']) + 1
            question=get_object_or_404(Question,pk=next_question_id)
            return render(request,'firstapp/test.html',{'question': question})
            #return HttpResponseRedirect(reverse('firstapp:test',args=(question,)))
    
    return render(request,'firstapp/test.html',{'question':question})
    

def result(request, result_id):
    result=ResultType.objects.get(pk=result_id)
    context={'result':result}
    return render(request,'firstapp/result.html',context)


# It returns an HttpResponse object 
# of the given template rendered with the given context.
def statistics(request):
    return HttpResponse("Your looking at the statistic page")