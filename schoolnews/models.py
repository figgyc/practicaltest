from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.DateTimeField()
    text =  models.CharField(max_length=2000)
