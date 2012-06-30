from django.db import models

class Post(models.Model):
    subject = models.CharField(max_length=30, blank=False)
    content = models.TextField(blank=False)
