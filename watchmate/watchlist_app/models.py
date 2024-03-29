from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.
  
class StreamPlatForm(models.Model):
    name = models.CharField(max_length = 50)
    about = models.TextField()
    website = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
    
class WatchList(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    active = models.BooleanField(default = True)
    platForm = models.ForeignKey(StreamPlatForm, on_delete = models.CASCADE, related_name = "watchlist")
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    rating = models.PositiveBigIntegerField(validators = [MinLengthValidator(1), MaxLengthValidator(5)])
    description = models.CharField(max_length = 200, null = True)
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)
    watchlist = models.ForeignKey(WatchList, on_delete = models.CASCADE, related_name = "reviews")
    
    def __str__(self):
        self.rating 