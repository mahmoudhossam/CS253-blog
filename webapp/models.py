from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    hashed_pw = models.CharField(max_length=100)
    salt = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

class Post(models.Model):
    subject = models.CharField(max_length=30)
    content = models.TextField()

def get_all_posts():
    return Post.objects.all()
