from django.contrib import admin  
from django.urls import path  
from web import views  
  
urlpatterns = [ 
    path('', views.index), 
    path('createclient/', views.createClient),
    path('getStudent/', views.student),
    path('studentClass/', views.studentClass.as_view()),
    # path('create_client/', views.createClient), 
]