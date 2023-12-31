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
        castingdirector = CastingDirector.objects.get(pk=pk)
        Project.objects.create(title=title, type=type, castingdirector=castingdirector)
        return redirect('casting_director_detail', pk=pk)

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

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title', 'type', 'location', 'description', 'castingdirector']
    template_name = "project_update.html"
    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})

class ProjectDelete(DeleteView):
    model = Project
    template_name = "project_delete_confirmation.html"
    success_url = "/projects/"

class ProjectDetail(DetailView):
    model = Project
    template_name = "project_detail.html"

class ProjectList(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context["projects"] = Project.objects.filter(title__icontains=title)
            context["header"] = f"Searching for {title}"
        else:
            context["projects"] = Project.objects.all() 
            context["header"] = "Trending Projects"

        return context

class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to The Network Homepage")

class About(View):
    def get(self, request):
        return HttpResponse("The Network About Page")
    
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"