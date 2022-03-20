from django.contrib import admin
from accounts.models import CustomUser, Balance, CoinAddress, Coin

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Balance)
admin.site.register(Coin)
admin.site.register(CoinAddress)
