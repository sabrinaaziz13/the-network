from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import CastingDirector
from django.views.generic.edit import CreateView



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
        name = self.request.GET.get("name")
        if name != None:
            context["casting_directors"] = CastingDirector.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:    
            context["casting_directors"] = CastingDirector.objects.all()
            context["header"] = "Casting Directors"
        return context 

class Profile(TemplateView):
    template_name = "profile.html"