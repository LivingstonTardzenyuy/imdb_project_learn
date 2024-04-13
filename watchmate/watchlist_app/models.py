from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User 
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
    total_reviews = models.IntegerField(default =0)
    average_rating = models.IntegerField(default =0)
     
    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    review_user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.PositiveBigIntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length = 200, null = True)
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)
    watchlist = models.ForeignKey(WatchList, on_delete = models.CASCADE, related_name = "reviews")
    
    def __str__(self):
        return str(self.rating) + " " + "-" + self.watchlist.name 