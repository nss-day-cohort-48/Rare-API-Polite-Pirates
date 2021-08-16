from django.db import models

class Comment(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    content = models.CharField( max_length=1000)
    created_on = models.DateTimeField()
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.content