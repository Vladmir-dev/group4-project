from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .serializers import NewsSerializer, WeatherSerializer
from .models import News, Weather
# Create your views here.


class NewsAPIView(GenericAPIView):
	serializer_class = NewsSerializer
	queryset = News.objects.all()

	def get(self, request, format=None):
		
		serializer = self.serializer_class(self.get_queryset(), many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)