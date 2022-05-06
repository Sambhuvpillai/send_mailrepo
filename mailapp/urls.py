from django.urls import path,include
from mailapp import views


urlpatterns = [
    path('',views.stdform,name='stdform'),
    
]
