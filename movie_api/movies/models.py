from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name=models.CharField(max_length=20)
    language=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    release=models.IntegerField()
    duration=models.IntegerField()
    rating=models.FloatField()
    