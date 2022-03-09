from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'occupation', 'phone', 'sex']


class CustomLoginSerializer(LoginSerializer):

    username = None