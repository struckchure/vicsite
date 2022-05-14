from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import request, HttpResponseRedirect, HttpResponse

from accounts.models import Balance
from transactions.models import Deposit, Withdraw
from investments.models import Investment
from transactions.forms import WithdrawForm, DepositForm
from accounts.models import Coin, CoinAddress
from accounts.models import CustomUser


# class DepositView(LoginRequiredMixin, CreateView):
#     """
#     This class handles the deposit request form
#     """
#     login_url = reverse_lazy("login")
#     form_class = DepositForm
#     # model = Deposit
#     # fields =  fields = ("coin", "package", "company_wallet_address", "amount", "proof",)
#     template_name = "transactions/deposit.html"
#     success_url = reverse_lazy("transactions")

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_invalid(form)

@login_required(login_url="/accounts/login")
def DepositView(request):
    if request.method == "POST":
        form = DepositForm(request.POST)
        message = "You have successfully placed a Deposit request.  Your account balance will be credited within the next 24 hours."

        if form.is_valid():
            form.save(request)
            messages.success(request, message)
            return HttpResponseRedirect(reverse_lazy("transactions"))
    else:
        form = DepositForm()
        print("Form not valid")
    return render(request, "transactions/deposit.html", {
        "form": form,
        "detail": CoinAddress.objects.all()
    })

class TransactionHistoryView(LoginRequiredMixin, TemplateView):
    """
    This class displays the Transaction history for a user
    """
    login_url = reverse_lazy("login")
    # model = Investment
    template_name = "transactions/transactions.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "user": self.request.user,
            "withdraw_h": Withdraw.objects.filter(user=self.request.user),
            "deposit_h": Deposit.objects.filter(user=self.request.user),
            "invest_h": Investment.objects.filter(user=self.request.user) 
        }
        return context
    

# class WithdrawView(CreateView):
#     """
#     This class handles the form for withdraw request
#     """

#     model = Withdraw
#     form_class = WithdrawForm
#     template_name = "transactions/withdrawal.html"
#     success_url = reverse_lazy("home")
    
    # extra_context = {
    #     "coin": Coin.objects.all(),
    #     "coin_ad": CoinAddress.objects.all(),
    # }

@login_required(login_url="/accounts/login")
def WithdrawView(request):
    if request.method == "POST":
        form = WithdrawForm(request.POST)
        message = "You have successfully placed a withdraw request.  Your wallet will be credited within the next 24 hours."
        if form.is_valid():
            form.save(request)
            messages.success(request, message)
            return HttpResponseRedirect(reverse_lazy("withdraw"))
    else:
        form = WithdrawForm()
    return render(request, "transactions/withdrawal.html", {
        "form": form,
    })
        




