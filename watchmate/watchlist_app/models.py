from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    active = models.BooleanField(default = True)
    
    
    def __str__(self):
        return self.name
    
    
class StreamPlatForm(models.Model):
    name = models.CharField(max_length = 50)
    about = models.TextField()
    website = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name