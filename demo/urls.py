from django.urls import path
from  . import views


urlpatterns = [
    
     path('',views.index),
     path('',views.buysell),
     path('',views.insidelayout),
     path('',views.chart),
     
     
    
    
]
