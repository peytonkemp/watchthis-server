from django.db import models

class Genre(models.Model):
    """Genre model
    fields:
        name (CharField): name of the game type
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name