from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import DueDate, AmountInvested, Contact, CustomUser, Balance, CoinAddress, Coin, Profilepic
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser


admin.site.register(CustomUser)
admin.site.register(Balance)
admin.site.register(Coin)
admin.site.register(CoinAddress)
admin.site.register(Contact)
admin.site.register(Profilepic)
admin.site.register(DueDate)
admin.site.register(AmountInvested)
