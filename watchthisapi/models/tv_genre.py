from django.db import models


class TvGenre(models.Model):
    """Join model for Genres and Tvs
    """
    name = models.CharField(max_length=50)
    tv = models.ForeignKey("Tv", on_delete=models.CASCADE)

    def __str__(self):
        return self.name