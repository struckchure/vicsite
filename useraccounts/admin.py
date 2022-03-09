from django.contrib import admin
from useraccounts.models import Coin, CoinAddress, Balance, Withdraw, Deposit
# Register your models here.

admin.site.register(Coin)
admin.site.register(CoinAddress)
admin.site.register(Balance)
admin.site.register(Withdraw)
admin.site.register(Deposit)
