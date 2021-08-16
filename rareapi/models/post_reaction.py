from django.db import models

class PostReaction(models.Model):
    """Reaction model
    fields:
       
    """
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    reaction_id = models.ForeignKey("Reaction", on_delete=models.CASCADE)

    def __str__(self):
        return self.reaction_id