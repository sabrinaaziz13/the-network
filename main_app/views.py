from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import CastingDirector

class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to The Network Homepage")

class About(View):
    def get(self, request):
        return HttpResponse("The Network About Page")
    
class Profile(View):
    def get(self, request):
        return HttpResponse("Your Profile")
    
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class CastingDirectorList(TemplateView):
    template_name = "casting_director_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["casting_directors"] = CastingDirector.objects.all()
        return context 

class Profile(TemplateView):
    template_name = "profile.html"

class CastingDirector:
    def __init__(self, name, img, bio):
        self.name = name
        self.img = img
        self.bio = bio


# casting_directors = [
#   CastingDirector("David Rapaport", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDEWvuedDrl1EwuXMg2y55NnVveB35tJqYyUVMuB3aOW4AlJOm", "Those who know, know. David has cast just about every popular teen-based drama on television in the last fifteen years."),
# ]
