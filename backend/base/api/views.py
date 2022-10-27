from distutils.command.build_scripts import first_line_re
from rest_framework_simplejwt.tokens import AccessToken ,RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.middleware import csrf
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login 
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from django.contrib.auth.models import User, Group
from .authenticate import CustomAuthentication
from .serializers import (RegisterSerializer , 
                        GetUserListSerializer)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data
        response = Response()        
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                    value = data["access"],
                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)
                response.data = {"Success" : "Login successfully","data":data}
                print(request.user)
                return response
            else:
                return Response({"No active" : "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid" : "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)


class RegisterUserAPIView(APIView):
    serializer_class = RegisterSerializer


class UpdateUserView(APIView):
    authentication_classes = [JWTAuthentication]

    def put(self, request):
        token=AccessToken(request.headers.get('Bearer'))
        user=User.objects.get(pk=token.payload.get("user_id"))
        # print(request.data, "payoad")
        first_name=request.data['first_name']
        last_name=request.data['last_name']
        email=request.data['email']
        if first_name:
            user.first_name=first_name
        if last_name:
            user.last_name=last_name
        if email:
            user.email=email
        user.save()    
        return Response("Updated Successfully")


class ViewUser(generics.ListAPIView):
    def get(self,request):
        token=AccessToken(request.headers.get('Bearer'))
        user=User.objects.get(pk=token.payload.get("user_id"))
        if user.groups.filter(name='staff').exists():
            # return User.objects.filter(name='user')
            user_list = Group.objects.filter(name="user").first()
            serializer_data=GetUserListSerializer(user_list.user_set.all(), many=True).data
            return Response(serializer_data)
        else:
            return Response("Only accessible to staff")

















