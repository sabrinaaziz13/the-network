from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('about/', views.About.as_view(), name="about"),
  path('projects/', views.Project.as_view(), name="project"),
  path('casting-directors/', views.CastingDirectorList.as_view(), name="casting_director_list"),
  path('casting-directors/new', views.CastingDirectorCreate.as_view(), name="casting_director_create"),
  path('casting-directors/<int:pk>/', views.CastingDirectorDetail.as_view(), name="casting_director_detail"),
  path('casting-directors/<int:pk>/update', views.CastingDirectorUpdate.as_view(), name="casting_director_update"),
  path('casting-directors/<int:pk>/delete', views.CastingDirectorDelete.as_view(), name="casting_director_delete"),
]