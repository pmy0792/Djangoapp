from django.urls import path
from firstapp import views

# routing information

app_name='firstapp'
urlpatterns = [
    path('',views.index, name='index'),
    path('test',views.test,name='test'),
    path('result/<question_id>',views.result,name='result'),
    path('statistics',views.statistics,name='statistics')
]
