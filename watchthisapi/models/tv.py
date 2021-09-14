from django.db import models


class Tv(models.Model):
    """Tv Model
    Fields:
    """
    name = models.CharField(max_length=100)
    backdrop_path = models.URLField()
    overview = models.TextField()
    popularity = models.IntegerField()
    poster_path = models.URLField()
    tagline = models.TextField()
    vote_average = models.IntegerField()

    def __str__(self):
        return self.name