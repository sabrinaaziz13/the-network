from django.db import models

class CastingDirector(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    bio = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
