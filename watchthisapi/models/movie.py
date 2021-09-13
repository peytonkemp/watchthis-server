from django.db import models


class Movie(models.Model):
    """Movie Model
    Fields:
    """
    title = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=150)
    overview = models.CharField(max_length=2000)
    popularity = models.IntegerField()
    poster_path = models.CharField(max_length=1000)
    release_date = models.DateField()
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    tagline = models.CharField(max_length=1000)
    vote_average = models.IntegerField()

    def __str__(self):
        return self.title