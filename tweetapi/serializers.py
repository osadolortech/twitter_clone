
from rest_framework import serializers
from .models import ProfileModel, Tweet_Model,CommentModels,LikeModel,RetweetModel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    tweet = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    like=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    retweet=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'id','first_name','last_name','username','tweet','comment','like','retweet'
        )



class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ProfileModel
        fields = (
            'id','user','Bio','Location','Birth_date'
        )
        

class TweetSerializer(serializers.ModelSerializer):
    
    comment = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    like=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    retweet=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Tweet_Model
        fields = (
            'id','owner','content','created_time','comment','like','retweet','number_of_likes','number_of_retweets'
        )    


class Commentserializer(serializers.ModelSerializer):
 
    class Meta:
        model = CommentModels
        fields = (
            'id','content','owner','created_time','tweet'
        )


class LikeSerializers(serializers.ModelSerializer):

    class Meta:
        model = LikeModel
        fields = (
            'id','owner','created_time','tweet'
        )

class RetweetSeriliazer(serializers.ModelSerializer):
  
    class Meta:
        model = RetweetModel
        fields = (
            'id','owner','created_time','tweet'
        )

        