from django.db import models


class Movie(models.Model):
    """Movie Model
    Fields:
    """
    title = models.CharField(max_length=100)
    backdrop_path = models.URLField()
    overview = models.TextField()
    popularity = models.IntegerField()
    poster_path = models.URLField()
    release_date = models.DateField()
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    tagline = models.TextField()
    vote_average = models.IntegerField()

    def __str__(self):
        return self.title