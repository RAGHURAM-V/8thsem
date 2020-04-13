from django.urls import path
from  . import views


urlpatterns = [
    
    path('', views.HomeView.as_view()), 
    path('api', views.ChartData.as_view()),
     path('',views.index),
     path('',views.buysell),
     path('',views.insidelayout),
     path('',views.chart),
     
     
    
    
]
