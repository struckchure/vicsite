from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from users.models import CustomUser, Balance, UserCryptoDetails
from users.models import SEX


class UserSerializer(RegisterSerializer):
    occupation = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=100)
    sex = serializers.ChoiceField(choices=SEX)

    username = None

    # class Meta:
    #     model = CustomUser
    #     fields = ['id', 'email', 'first_name', 'last_name', 'occupation', 'phone', 'sex']

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.gender = self.data.get('occupation')
        user.gender = self.data.get('phone')
        user.phone_number = self.data.get('sex')
        user.save()
        return user


class CustomLoginSerializer(LoginSerializer):

    username = None

class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('balance',)

class UserCryptoDetails(serializers.ModelSerializer):
    class Meta:
        model = UserCryptoDetails
        fields = ('coin', 'wallet_address',)