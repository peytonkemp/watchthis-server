from django.db import models
from django.contrib.auth.models import User

class Watchlist(models.Model):
    """Genre model
    fields:
        name (CharField): name of the game type
    """
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name