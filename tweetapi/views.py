from rest_framework import generics
from .models import ProfileModel
from django.contrib.auth.models import User
from .serializers import ProfileSerializer,UserSerializer

class Userview(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class ProfileViews(generics.ListCreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class ProfileDetails(generics.RetrieveDestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer


