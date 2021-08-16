from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField, DateField, DateTimeField
from django.db.models.fields.files import ImageField


class RareUser(models.Model):
    """Rare User Model
    Args:
        models (OneToOneField): The rare user information for the gamer
        bio (CharField): The bio of the rare user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    profile_img = ImageField()
    active = BooleanField()
    created_on = DateTimeField()

    def __str__(self):
        return self.user.username     