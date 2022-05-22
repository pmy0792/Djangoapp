import sqlite3
from .models import *

mbti_and_result={
    'ESFJ':'Coffee Shop Barista',
    'ENTJ':'Cinema Staff',
    'ISTJ':'General Assistant',
    'ESFP':'LUSH Staff',
    'ENFP':'Amusement Park Staff',
    'ISTP':'Convenience Store Staff',
    'INFJ':'Office Assistant',
    'ISFJ':'Wedding Guest',
    'ISFP':'Bakery Staff',
    'INTP':'Blogger',
    'INTJ':'Private Tutor',
    'ESTJ':'Exam Supervisor',
    'ESTP':'Folk Village Staff',
    'INFP':'Pet Sitter',
    'ENTP':'Academy Instructor',
    'ENFJ':'Kids Cafe Staff'  
}

question_num=12
def calc_result(user):
    points={'EI':0, 'NS':0,'TF':0,'JP':0}
    vote=Voting.objects.filter(user_ip__user_ip=user).values('choice','question')
    #choice=list(vote.values('choice'))[-12:] # the latest 12 choices of the user
    
    q_and_c=vote.order_by('-id')[:question_num]
    
    for qc in q_and_c:
        q=Question.objects.get(pk=qc['question'])
        c=Choice.objects.get(pk=qc['choice'])
        q_type=q.question_type
        c_point=c.choice_point
        points[q_type]+=c_point
        
    mbti_type=""
    for key in points.keys():
        mbti_type += (key[0] if points[key]>=2 else key[1])
        
    result_type=mbti_and_result[mbti_type]
    result_type=ResultType.objects.get(title=result_type)
    return result_type