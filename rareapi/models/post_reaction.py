from django.db import models

class PostReaction(models.Model):
    """Reaction model
    fields:
       
    """
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    rare_user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    reaction = models.ForeignKey("Reaction", on_delete=models.CASCADE)

    def __str__(self):
        return self.reaction