from django.db import models

class Post(models.Model):
    subject = models.CharField(max_length=30, blank=False)
    content = models.TextField(blank=False)

def get_all_posts():
    return Post.objects.all()
