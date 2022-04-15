from django.urls import path
from firstapp import views

# routing information

urlpatterns = [
    path('',views.index),
    path('home/',views.index),
    path('result/<type>',views.result)
]
