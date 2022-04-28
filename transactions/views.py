from django.views.generic import ListView, CreateView, TemplateView
from accounts.models import Balance
from transactions.models import Deposit, Withdraw
from investments.models import Investment
from transactions.forms import WithdrawForm, DepositForm
# from accounts.models import CustomUser


class DepositView(CreateView):
    """
    This class handles the deposit request form
    """

    model = Deposit
    form_class = DepositForm
    template_name = "transactions/deposit.html"


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
    
    # extra_context = {
    #     "wallet_bal": Balance.objects.all()
    # }





