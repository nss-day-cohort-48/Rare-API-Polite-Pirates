from rareapi.models import category
from django.db import models


class Post(models.Model):
    """Post Model
    Fields:
        
    """
    title = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    rare_user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    publication_date = models.DateTimeField()
    image_url = models.ImageField() #install "pip install Pillow" 
    content = models.CharField(max_length=500)
    approved = models.BooleanField()

    def __str__(self):
        return self.title


#Install instructions for local image uploads. https://www.geeksforgeeks.org/imagefield-django-models/