from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=345)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
  
    def __str__(self): 
        return self.name