from .models import News, Weather
from rest_framework import serializers

class NewsSerializer(serializers.ModelSerializer):
	image = serializers.ImageField(
        max_length=None, use_url=True,
    )

	class Meta:
		model = News
		fields = '__all__'

class WeatherSerializer(serializers.ModelSerializer):
	image = serializers.ImageField(
        max_length=None, use_url=True,
    )
    
	class Meta:
		model = Weather
		fields = '__all__'