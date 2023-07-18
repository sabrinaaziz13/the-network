from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import CastingDirector, Project
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

class CastingDirectorCreate(CreateView):
    model = CastingDirector
    fields = ['name', 'img', 'bio']
    template_name = "casting_director_create.html"
    success_url = "/casting-directors/"

    def get_success_url(self):
        return reverse('casting_director_detail', kwargs={'pk': self.object.pk})

class CastingDirectorUpdate(UpdateView):
    model = CastingDirector
    fields = ['name', 'img', 'bio']
    template_name = "casting_director_update.html"
    
    def get_success_url(self):
        return reverse('casting_director_detail', kwargs={'pk': self.object.pk})

class CastingDirectorDelete(DeleteView):
    model = CastingDirector
    template_name = "casting_director_delete_confirmation.html"
    success_url = "/casting-directors/"

class CastingDirectorDetail(DetailView):
    model = CastingDirector
    template_name = "casting_director_detail.html"

class ProjectCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        type = request.POST.get("type")
        casting_director = CastingDirector.objects.get(pk=pk)
        Project.objects.create(title=title, type=type, casting_director=casting_director)
        return redirect('casting_director_detail', pk=pk)

class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to The Network Homepage")

class About(View):
    def get(self, request):
        return HttpResponse("The Network About Page")
    
class Project(View):
    def get(self, request):
        return HttpResponse("Project")
    
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

class Project(TemplateView):
    template_name = "project.html"