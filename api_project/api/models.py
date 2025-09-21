from django.db import models

class BooK(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    

# Create your models here.
