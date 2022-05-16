from django.urls import path
from firstapp import views

# routing information

urlpatterns = [
    path('',views.index, name='index'),
    path('result/<id>',views.result,name='result'),
    path('statistics',views.statistics,name='statistics')
]
