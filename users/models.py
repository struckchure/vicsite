from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager

from useraccounts.models import Balance, Coin, CoinAddress

SEX = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    occupation = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    sex = models.CharField(max_length=100, choices=SEX)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['occupation', 'phone', 'sex']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserCryptoDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=500)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)