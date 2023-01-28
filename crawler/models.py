from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crawler(models.Model):
    crawler_name = models.CharField(max_length=100)
    crawler_url = models.URLField(max_length=200)
    crawler_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.crawler_name


class Attribute(models.Model):
    attribute_key = models.CharField(max_length=150)
    attribute_value = models.CharField(max_length=200)
    attribute = models.ForeignKey(Crawler, on_delete=models.CASCADE, related_name="crawler_attribute")
    
    def __str__(self) -> str:
        return self.attribute_key
