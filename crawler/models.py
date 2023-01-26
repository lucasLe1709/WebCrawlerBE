from django.db import models

# Create your models here.
class Crawler(models.Model):
    crawler_name = models.CharField(max_length=100)
    crawler_url = models.URLField(max_length=200)


class Attribute(models.Model):
    attribute_key = models.CharField(max_length=150)
    attribute_value = models.CharField(max_length=200)
    attribute = models.ForeignKey(Crawler, on_delete=models.CASCADE, related_name="crawler_attribute")
