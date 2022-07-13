
from django.urls import path
from .import views

#controls all projects url paths
urlpatterns = [
    path('', views.projects, name="projects"),
    path('projects/', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    
]
