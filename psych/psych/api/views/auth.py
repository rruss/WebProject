import json

from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import status

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    usser = User.objects.get(username=user)
    serializer = UserSerializer(usser)
    id = serializer.data['id']
    token, created = Token.objects.get_or_create(user=user)
    user_new = User.objects.filter(username=request.data.get('username'))
    # return  Response({})
    return Response({'token': token.key,
                     'id': id})

@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)