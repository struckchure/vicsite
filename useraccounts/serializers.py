from rest_framework import serializers
from useraccounts.models import Deposit, Withdraw, Balance

class DepositHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('id', 'coin', 'company_wallet_address', 'amount', 'proof', 'transaction_date', 'status',)

class DepositFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('coin', 'company_wallet_address', 'amount', 'proof',)

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw 
        fields = ('coin', 'wallet_address', 'amount',)

class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('balance',)