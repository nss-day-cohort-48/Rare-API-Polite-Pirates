from django.db import models

class Reaction(models.Model):
    """Reaction model
    fields:
       
    """
    label = models.CharField(max_length=50)
    image_url = models.ImageField()

    def __str__(self):
        return self.label