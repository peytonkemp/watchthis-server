from django.db import models


class MovieGenre(models.Model):
    """Join model for Genres and Movies
    """
    name = models.CharField(max_length=50)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.name