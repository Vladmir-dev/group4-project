from .models import News, Weather
from rest_framework import serializers

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = '__all_'

class WeatherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Weather
		fields = '__all__'