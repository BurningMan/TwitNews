from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=140)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    datetime = models.CharField(max_length=30)
    avatar = models.CharField(max_length=400)
