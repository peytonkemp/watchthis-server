from django.db import models


class TvGenreJoin(models.Model):
    """Join model for Genres and Tvs
    """
    tv = models.ForeignKey("Tv", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
