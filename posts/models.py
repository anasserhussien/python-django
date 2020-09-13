from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify 

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 120)
    slug = models.SlugField(unique = True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

# a recursive method to produce a slug before saving the instance
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug = slug).order_by("-id")
    if qs.exists():
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug)
    
    return slug
        


@receiver(pre_save, sender = Post)
def pre_save_post_signal(sender, instance, *args, **kwargs):
    if not instance.slug: # to keep original slug if title is being updated
        instance.slug = create_slug(instance)
