from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from accounts.models import LastDeposit, AmountInvested, Profilepic, Contact, CustomUser, Balance, UserCryptoDetails, Coin, CoinAddress

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "firstname", "lastname", "occupation", "phone", "sex")


# Source: https://morioh.com/p/fe0e3a395d8b

class CoinOption(serializers.ModelSerializer):
    class Meta:
        model = Coin 
        fields = "__all__"


class CoinAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinAddress
        fields = "__all__"

class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ("balance",)


class UserCryptoDetailsSerializer(serializers.ModelSerializer):
    '''
    User ought to enter his or her coin/coin address or wallet/ wallet id
    '''
    class Meta:
        model = UserCryptoDetails
        fields = (
            "coin",
            "wallet_address",
        )

class ContactUS(serializers.ModelSerializer):
    ''' Contact us form '''

    class Meta:
        model = Contact
        fields = (
            "c_email",
            "msg",
        )

class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profilepic
        fields = "__all__"

class LastDepositSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LastDeposit
        fields = "__all__"

class AmountInvestedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AmountInvested
        fields = "__all__"