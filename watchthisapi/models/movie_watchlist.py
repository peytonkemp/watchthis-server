from watchthisapi.models import movie
from django.db import models


class MovieWatchlist(models.Model):
    """Join model for Genres and Tvs
    """
    watchlist = models.ForeignKey("Watchlist", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
