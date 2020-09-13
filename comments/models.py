from django.db import models
from django.conf import settings

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.content