from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('about/', views.About.as_view(), name="about"),
  path('casting-directors/', views.CastingDirector.as_view(), name="casting_director_list"),
  path('profile/', views.Profile.as_view(), name="profile"),
]