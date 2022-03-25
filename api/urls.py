from django.urls import path
from .views import NewsAPIView
from django.urls import re_path as url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="newsfeed api")

urlpatterns = [
    url(r'^$', schema_view),
    path('news/', NewsAPIView.as_view(), name="news"),
]
