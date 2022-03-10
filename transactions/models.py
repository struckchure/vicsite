from django.conf import settings
from django.db import models
from users.models import Coin, CoinAddress, Balance
from investments.models import Investment

STATUS = (
    ('P', 'Pending'),
    ('F', 'Failed'),
    ('C', 'Completed'),
)

INVEST_STATUS = (
    ('A', 'Active'),
    ('N', 'Unactive'),
)

# Not Funtional
class TransactionHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sn = models.PositiveIntegerField()
    # deposit_

class Withdraw(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)
    coin = models.ForeignKey(CoinAddress, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=500)
    amount = models.CharField(max_length=100, null=True)
    status = models.ForeignKey(WithdrawStatus, on_delete=models.CASCADE, choices=STATUS, null=True)

class Deposit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    company_wallet_address = models.ForeignKey(CoinAddress, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)
    proof = models.ImageField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(DepositStatus, on_delete=models.CASCADE, choices=STATUS, null=True)

class DepositStatus(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deposit_status = models.CharField(max_length=20, choices=STATUS)

class WithdrawStatus(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    withdraw_status = models.CharField(max_length=20, choices=STATUS)

class InvestmentStatus(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    invest_status = models.CharField(max_length=20, choices=INVEST_STATUS)