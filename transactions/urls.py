from django.urls import path, include
from transactions.views import DepositHistoryView, DepositView, WithdrawHistory, WithdrawView

urlpatterns = [
    path('deposit/', DepositView.as_view()),
    path('deposit/history/', DepositHistoryView.as_view()),
    path('withdraw/', WithdrawView.as_view()),
    path('withdraw/history/', WithdrawHistory.as_view()),

]
