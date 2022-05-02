from django.views.generic import ListView, CreateView, TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import request, HttpResponseRedirect, HttpResponse

from accounts.models import Balance
from transactions.models import Deposit, Withdraw
from investments.models import Investment
from transactions.forms import WithdrawForm, DepositForm
from accounts.models import Coin, CoinAddress
# from accounts.models import CustomUser


class DepositView(CreateView):
    """
    This class handles the deposit request form
    """

    model = Deposit
    form_class = DepositForm
    template_name = "transactions/deposit.html"

# def DepositView(request):
    # if request.method == "POST":
        # form = DepositForm(request.POST)
# 
        # if form.is_valid():
            # form.save(request)
            # return HttpResponse("It is saved")
    # else:
        # form = DepositForm()
    # # return render(request, "transactions/deposit.html", {"form": form})

class TransactionHistoryView(TemplateView):
    """
    This class displays the Transaction history for a user
    """
    # model = Investment
    template_name = "transactions/transactions.html"

    extra_context = {
        "withdraw_h": Withdraw.objects.all(),
        "deposit_h": Deposit.objects.all(),
        "invest_h": Investment.objects.all(),
    }

class WithdrawView(CreateView):
    """
    This class handles the form for withdraw request
    """

    model = Withdraw
    form_class = WithdrawForm
    template_name = "transactions/withdrawal.html"
    success_url = reverse_lazy("home")
    
    # extra_context = {
    #     "coin": Coin.objects.all(),
    #     "coin_ad": CoinAddress.objects.all(),
    # }

# def WithdrawView(request):
#     if request.method == "POST":
        
#         form = WithdrawForm(request.POST or None)
#         if form.is_valid():
#             form.save(request)




