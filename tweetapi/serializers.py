from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import ProfileModel, Tweet_Model, CommentModels
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    pass

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProfileModel
        fields = (
            'id', 'first_name','last_name','Bio','Location','Birth_date'
        )

class TweetSerializer(serializers.ModelSerializer):
    comment = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Tweet_Model
        fields = '__all__'

class Commentserializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CommentModels
        fields = (
            'id','body','owner','created_time'
        )
