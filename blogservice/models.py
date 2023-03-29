from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Posts(models.Model):
    user_id = models.IntegerField()
    description = models.TextField()
    text = models.TextField()
    likes = models.IntegerField()
    views = models.IntegerField()

    def __str__(self):
        return self.description

class Likes(models.Model):
    userid = models.IntegerField()
    postid = models.IntegerField()


class Comments(models.Model):
    post_id = models.IntegerField()
    author_id = models.IntegerField()
    text = models.TextField()
    likes = models.IntegerField()

