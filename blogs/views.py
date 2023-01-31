from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from blogs import models
from blogs import serializers


class BlogView(ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BolgSerializer
