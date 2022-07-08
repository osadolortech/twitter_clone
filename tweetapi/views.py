from rest_framework import generics
from .models import ProfileModel,LikeModel,Tweet_Model,CommentModels,RetweetModel
from django.contrib.auth.models import User
from .serializers import ProfileSerializer,UserSerializer,TweetSerializer,Commentserializer,LikeSerializers,RetweetSeriliazer

class Userview(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class= UserSerializer

class ProfileViews(generics.ListCreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

class TweetView(generics.ListCreateAPIView):
    queryset= Tweet_Model.objects.all()
    serializer_class = TweetSerializer

class TweetDetails(generics.RetrieveDestroyAPIView):
    queryset = Tweet_Model.objects.all()
    serializer_class = TweetSerializer

class CommentView(generics.ListCreateAPIView):
    queryset = CommentModels.objects.all()
    serializer_class = Commentserializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class LikeTWEET(generics.ListCreateAPIView):
    queryset=LikeModel.objects.all()
    serializer_class=LikeSerializers

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class RetweetView(generics.ListCreateAPIView):
    queryset=RetweetModel.objects.all()
    serializer_class=RetweetSeriliazer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

