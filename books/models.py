from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    content = models.TextField(blank=True,null=True)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    price = models.CharField(max_length=12)

    def __str__(self):
        return self.title
    
    
    

