from django.views.generic import ListView, CreateView, TemplateView
from transactions.models import Deposit, Withdraw
from investments.models import Investment
# from accounts.models import CustomUser


class DepositView(CreateView):
    """
    This class handles the deposit request form
    """

    model = Deposit
    template_name = "transactions/deposit.html"
    fields = ["user", "coin", "package", "company_wallet_address", "amount", "proof", "transactions_date", "status",]

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
    fields = ["user", "coin", "wallet_address", "amount", "transaction_date", "status",]
    template_name = "transactions/withdrawal.html"





