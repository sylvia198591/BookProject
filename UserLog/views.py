from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
# from pyparsing import unicode
# from requests import Response
from rest_framework.generics import *
from UserLog.models import *
from UserLog.serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class ExampleView(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
})