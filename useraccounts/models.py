from django.conf import settings
from django.db import models
from transactions.models import DepositStatus, WithdrawStatus

STATUS = (
    ('P', 'Pending'),
    ('F', 'Failed'),
    ('C', 'Completed'),
)


# Admin will be able to specify the available coin and it's wallet address
class Coin(models.Model):
    coin_type = models.CharField(max_length=20)

    def __str__(self):
        return self.coin_type


class CoinAddress(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    coin_wallet_address = models.CharField(max_length=500)

    def __str__(self):
        return self.coin

    
# Sets the user's balance
class Balance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField()


class Withdraw(models.Model):
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

class UserCryptoDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=500)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)

