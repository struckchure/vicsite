from rest_framework import serializers
from transactions.models import Deposit, Withdraw


class DepositHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = (
            "id",
            "coin",
            "package",
            "company_wallet_address",
            "amount",
            "proof",
            "transaction_date",
            "status",
        )


class DepositFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = (
            "package",
            "coin",
            "company_wallet_address",
            "amount",
            "proof",
        )


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = (
            "coin",
            "wallet_address",
            "amount",
        )

class WithdrawHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = (
            "id",
            "coin",
            "wallet_address",
            "amount",
            "transaction_date",
            "status",
        )
