from django.db import models


class MovieGenre(models.Model):
    """Join model for Genres and Movies
    """
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
