from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('about/', views.About.as_view(), name="about"),
  path('casting-directors/', views.CastingDirectorList.as_view(), name="casting_director_list"),
  path('casting-directors/new', views.CastingDirectorCreate.as_view(), name="casting_director_create"),
  path('casting-directors/<int:pk>/', views.CastingDirectorDetail.as_view(), name="casting_director_detail"),
  path('casting-directors/<int:pk>/update', views.CastingDirectorUpdate.as_view(), name="casting_director_update"),
  path('casting-directors/<int:pk>/delete', views.CastingDirectorDelete.as_view(), name="casting_director_delete"),
  path('casting-directors/<int:pk>/projects/new', views.ProjectCreate.as_view(), name="project_create"),
  path('projects/', views.ProjectList.as_view(), name="project_list"),
  path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project_detail"),
  path('projects/<int:pk>/update', views.ProjectUpdate.as_view(), name="project_update"),
  path('projects/<int:pk>/delete', views.ProjectDelete.as_view(), name="project_delete"),
]