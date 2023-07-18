from django.db import models

class CastingDirector(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    bio = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Project(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    union = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    castingdirector = models.ForeignKey(CastingDirector, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return self.title
    