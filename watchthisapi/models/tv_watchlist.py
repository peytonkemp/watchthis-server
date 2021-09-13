from watchthisapi.models import tv
from django.db import models


class TvWatchlist(models.Model):
    """Join model for Genres and Tvs
    """
    watchlist = models.ForeignKey("Watchlist", on_delete=models.CASCADE)
    tv = models.ForeignKey("Tv", on_delete=models.CASCADE)
