from rest_framework import serializers
from crawler.models import Crawler, Attribute


class AttributeSerializer(serializers.ModelSerializer):
    key = serializers.CharField(source='attribute_key')
    value = serializers.CharField(source='attribute_value')
    class Meta:
        model = Attribute
        fields = ['key', 'value']
        
class CrawlerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="crawler_name")
    url = serializers.URLField(source="crawler_url")
    attributes = AttributeSerializer(many=True, source="crawler_attribute")
    class Meta:
        model = Crawler
        fields = ['name', 'url', 'attributes']