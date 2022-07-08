import datetime
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login,authenticate,logout
import jwt

class Login(generics.CreateAPIView):
    serializer_class=UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error":"please fill all fileds"}, status=status.HTTP_400_BAD_REQUEST)
        check_user= User.objects.filter(username=username)
        if check_user == False:
            return Response({"error":"username does not exsit"}, status=status.HTTP_404_NOT_FOUND)
        user = authenticate(username=username, password=password) 
        if user is not None:
            login(request,user)
            payload = {
                'id': user.id,
                'exp': datetime.timedelta(minutes=20) + datetime.datetime.utcnow(),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload,'secret',algorithm='HS256')
            response = Response()
            response.set_cookie(key='jwt',value=token, httponly=True)
            response.data={
                'jwt':token,
            }
            return response
        else:
            error = {"Error": status.HTTP_400_BAD_REQUEST, "Error_message":"Invalid Username"}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

class UserloginView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            return Response({"error":"Authentication fail"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            payload = jwt.decode(token,'secret',algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return Response({"error":"Authentication fail"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class Logout(APIView):
    def get(self,request):
        logout(request)
        return Response("sucessfully logout")

