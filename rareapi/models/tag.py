from django.db import models

class Tag(models.Model):
    """Reaction model
    fields:
       
    """
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label