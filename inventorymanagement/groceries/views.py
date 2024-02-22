from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginUserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message':'Something went wrong'})
        
        serializer.save()
        user = User.objects.get(username= serializer.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({'status':200, 'payload': serializer.data,'token': str(token), 'message': 'you data is registered'})

class LoginView(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data,context={'request': request})
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message':'Something went wrong'})
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'status': 401, 'message': 'Invalid credentials'})

        token, created = Token.objects.get_or_create(user=user)

        return Response({'status': 200, 'token': str(token), 'message': 'Login successful'})
    
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete() 
        return Response({'status': 200, 'message': 'Logout successful'})