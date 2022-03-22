from django.contrib import admin
from transactions.models import Deposit, Withdraw
# Register your models here.

admin.site.register(Deposit)
admin.site.register(Withdraw)