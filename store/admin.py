from django.contrib import admin

# Register your models here.

from store.models import UserProfile, Movie, MovieRented

admin.site.register(UserProfile)
admin.site.register(Movie)
admin.site.register(MovieRented)