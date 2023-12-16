from datetime import datetime, timedelta

from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Movie(models.Model):
    lector = "Lektor";
    original = "Oryginalna"
    dubbing = "Dubbing"
    choices = [(lector,"Lektor"),(original,"Oryginalna"),(dubbing,"Dubbing")]
    age_choices = [(0,"Brak"),(7,"Od 7 roku życia"),(18,"Od 18 roku życia")]
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    minimum_age = models.IntegerField(default=0, choices=age_choices)
    soundtrack = models.CharField(max_length=10, choices=choices)
    language = models.CharField(max_length=100,)
    description = models.TextField(max_length=10000)
    subtitles = models.BooleanField(default=False)
    subtitles_language = models.CharField(max_length=100, null=True, default=None)
    picture_url = models.CharField(max_length=300)
    def __str__(self):
          return "%s" % self.title



def get_deadline():
    return datetime.today() + timedelta(days=7)
class MovieRented(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(default= get_deadline())




class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    coins = models.IntegerField(default=100)
    birth_date = models.DateField(default=datetime.now())

    def __str__(self):
          return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
