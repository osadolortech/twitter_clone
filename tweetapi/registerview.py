
from .registerSerializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer


class RegisterUserApi(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message":"User created sucessfuly. Now perform login to get your token"
        })
