from django.db import models

class PostTag(models.Model):
    """Join model for post and tags
    """
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE)
    reaction_id = models.ForeignKey("Reaction", on_delete=models.CASCADE)