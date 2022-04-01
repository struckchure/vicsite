from django.contrib import admin
from accounts.models import DueDate, AmountInvested, Contact, CustomUser, Balance, CoinAddress, Coin, Profilepic

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Balance)
admin.site.register(Coin)
admin.site.register(CoinAddress)
admin.site.register(Contact)
admin.site.register(Profilepic)
admin.site.register(DueDate)
admin.site.register(AmountInvested)
