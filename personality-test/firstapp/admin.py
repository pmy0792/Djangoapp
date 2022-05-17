from django.contrib import admin
from .models import Question,Choice,User,Voting

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)
admin.site.register(Voting)