from rest_framework import serializers
from . import models


class BolgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = '__all__'
