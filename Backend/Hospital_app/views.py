from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.models import User
from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status
from .models import *

# Create your views here.

# Usertable Views
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Register_User
@api_view(["POST"])
def register(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        user_data = {
            field: data
            for (field, data) in request.DATA.items()
            if field in VALID_USER_FIELDS
        }
        user_data.update()
        user = User_table().objects.create_user(**user_data)
        return Response(
            UserSerializer(instance=user).data, status=status.HTTP_201_CREATED
        )
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
