# coding: utf-8
from rest_framework import serializers
from .models import Gasoline, HighOctane, Diesel


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Gasoline and HighOctane and Diesel
        fields = ('rank', 'pref', 'price', 'date')
