from django.db import models

from crawler.models import Crawler

# Create your models here.
class User(models.Model):   
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    
    crawler = models.ForeignKey(Crawler, on_delete=models.CASCADE, related_name="user")
    


