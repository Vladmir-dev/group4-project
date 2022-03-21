from django.db import models

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=200)
	image = models.FileField()
	body = models.CharField(max_length=2000)
	date = models.DateTimeField()


class Weather(models.Model):
	title = models.CharField(max_length=255)
	image = models.FileField()
	description = models.CharField(max_length=255)
	date = models.DateTimeField()