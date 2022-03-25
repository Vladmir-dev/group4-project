from django.db import models

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images')
	body = models.CharField(max_length=2000)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__ (self):
		return self.title

	class Meta:
		verbose_name_plural = "news"



class Weather(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='images')
	description = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__ (self):
		return self.title

	class Meta:
		verbose_name_plural = "weather"