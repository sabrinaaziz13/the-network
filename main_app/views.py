from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to The Network Homepage")

class About(View):
    def get(self, request):
        return HttpResponse("The Network About Page")
    
class CastingDirector(View):
    def get(self, request):
        return HttpResponse("The Network's Casting Directors")
    
class Profile(View):
    def get(self, request):
        return HttpResponse("Your Profile")
    
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class CastingDirector(TemplateView):
    template_name = "casting_director_list.html"

class Profile(TemplateView):
    template_name = "profile.html"