from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField
from accounts.managers import CustomUserManager


SEX = (
    ("Male", "Male"),
    ("Female", "Female"),
)

OCCUPATION = (
    ("Student", "Student"),
    ("Employed", "Employed"),
    ("Unemployed", "Unemployed"),
    ("Self-Employed", "Self-Employed"),
    ("Others", "Others"),
)

STATUS = (
    ("Pending", "Pending"),
    ("Failed", "Failed"),
    ("Completed", "Completed"),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, null=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    occupation = models.CharField(max_length=100, choices=OCCUPATION)
    phone = models.CharField(max_length=15)
    sex = models.CharField(max_length=20, choices=SEX)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname", "occupation", "phone", "sex"]

    objects = CustomUserManager()

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

# Admin will be able to specify the available coin and it's wallet address
class Coin(models.Model):
    coin_type = models.CharField(max_length=20)

    def __str__(self):
        return self.coin_type


# Address of the parent coin
class CoinAddress(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    coin_wallet_address = models.CharField(max_length=500)

    def __str__(self):
        return self.coin.coin_type


# Sets the user's balance
class Balance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.CharField(max_length=50)

    def __str__(self):
        return "{} {} || {}".format(self.user.firstname, self.user.lastname, self.user.email)

# User crypto details are being stored here
class UserCryptoDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    coin = models.CharField(max_length=400)
    wallet_address = models.CharField(max_length=500)

    def __str__(self):
        return "{} {} || {}".format(self.user.firstname, self.user.lastname, self.user.email)

class Contact(models.Model):
    c_email = models.EmailField(max_length=254)
    msg = models.CharField(max_length=50)
    
    def __str__(self):
        return self.c_email

class Profilepic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = CloudinaryField('image')

    def __str__(self):
        return "{} {} || {}".format(self.user.firstname, self.user.lastname, self.user.email)

class LastDeposit(models.Models):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amt = models.CharField(max_length=50)   

    def __str__(self):
        return "{} {} || {}".format(self.user.firstname, self.user.lastname, self.user.email) 

class AmountInvested(models.Models):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amt = models.CharField(max_length=50)   

    def __str__(self):
        return "{} {} || {}".format(self.user.firstname, self.user.lastname, self.user.email) 