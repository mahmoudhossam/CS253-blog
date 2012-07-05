from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    hashed_pw = models.CharField(max_length=100)
    salt = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

class Post(models.Model):
    subject = models.CharField(max_length=30)
    content = models.TextField()

def get_all_posts():
    return Post.objects.all()

def get_user(user_id):
    return User.objects.get(id=user_id)
