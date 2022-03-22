from django.contrib import admin
from transactions.models import InvestmentStatus, Withdraw
# Register your models here.

admin.site.register(InvestmentStatus)
admin.site.register(Withdraw)