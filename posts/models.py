from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 120)
    slug = models.SlugField(unique = True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __STR__(self):
        return self.title
    