from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from accounts.models import CustomUser, Balance, UserCryptoDetails

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "firstname", "lastname", "occupation", "phone", "sex")


# Source: https://morioh.com/p/fe0e3a395d8b


class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ("balance",)


class UserCryptoDetails(serializers.ModelSerializer):
    class Meta:
        model = UserCryptoDetails
        fields = (
            "coin",
            "wallet_address",
        )
