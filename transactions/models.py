from django.conf import settings
from django.db import models
from accounts.models import Coin, CoinAddress, Balance
from investments.models import Package

STATUS = (
    ("P", "Pending"),
    ("F", "Failed"),
    ("C", "Completed"),
)

INVEST_STATUS = (
    ("A", "Active"),
    ("N", "Unactive"),
)

# Not Funtional
class TransactionHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sn = models.PositiveIntegerField()
    # deposit_


class DepositStatus(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    deposit_status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.user


class WithdrawStatus(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    withdraw_status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.withdraw_status


class InvestmentStatus(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    invest_status = models.CharField(max_length=20, choices=INVEST_STATUS)

    def __str__(self):
        return self.invest_status


class Withdraw(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    # balance = models.ForeignKey(Balance, on_delete=models.CASCADE)
    coin = models.ForeignKey(CoinAddress, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=500)
    amount = models.CharField(max_length=100, null=True)
    transaction_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, choices=INVEST_STATUS, null=True)

    def __str__(self):
        return self.user


class Deposit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    company_wallet_address = models.ForeignKey(CoinAddress, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)
    proof =models.CharField(max_length=800)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default="status")

    # def __str__(self):
    #     return self.user
