from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200) #human readable name
    
    def __str__(self):
        return "Question: "+self.question_text
    
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0) 
    
    def __str__(self):
        return "Choice: "+ self.choice_text
    
class User(models.Model):
    user_ip=models.CharField(max_length=24)
    def __str__(self):
        return "User: "+self.user_ip
    
class Voting(models.Model):
    user_ip=models.ForeignKey(User,on_delete=models.DO_NOTHING,default="0.0.0.0")
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.ForeignKey(Choice,on_delete=models.CASCADE)
    
    def __str__(self):
        return "Voting: {} user voted {} in '{}'' Question".format(self.user_ip, self.choice, self.question)