from django.db import models

class WordPair(models.Model):
    korean = models.CharField(max_length=100)
    english = models.CharField(max_length=100)
# Create your models here.
