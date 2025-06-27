from .models import Rubric, Bb
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    '''Поля для API'''

    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')


class CategorySerializer(serializers.ModelSerializer):
    '''Поля для API'''
    model = Rubric
    fields = ('id', 'name')