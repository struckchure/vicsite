from django.urls import path
from transactions.views import (
    DepositView,
    TransactionHistoryView,
    WithdrawView,
)

urlpatterns = [
    path("deposit/", DepositView, name="deposit"),
    path("", TransactionHistoryView.as_view(), name="transactions"),
    path("withdraw/", WithdrawView, name="withdraw"),
]
