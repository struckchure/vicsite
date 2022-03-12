from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager

SEX = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    email = models.EmailField(_('email address'), unique=True)
    occupation = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    sex = models.CharField(max_length=100, choices=SEX)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'occupation', 'phone', 'sex']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email

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
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class UserCryptoDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=500)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)


