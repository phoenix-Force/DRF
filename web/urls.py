from django.contrib import admin  
from django.urls import path  
from web import views  
from web.viewes import student #student view
from web.viewes import studeViewApi #student view
from web.viewes import studentVAC #student view
urlpatterns = [ 
    path('', views.index), 
    # path('createclient/', views.createClient),
    # path('getStudent/', views.student),
    # path('studentClass/', views.studentClass.as_view()),
    # path('create_client/', views.createClient), 
    path('create-student/', student.studentClass.as_view()),
    path('studentself/<int:id>', student.studentClass.as_view()),
    path('studeva/<int:id>', studeViewApi.getStudent),
    path('studeva/', studeViewApi.getStudent),
    path('studentVAC/', studentVAC.StudentAPI.as_view()),
    path('studentVAC/<int:id>', studentVAC.StudentAPI.as_view())
]