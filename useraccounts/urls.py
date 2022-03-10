from django.urls import path
from useraccounts.views import DepositHistoryView, WithdrawView, DepositView, UserBalanceView, UserAssetView


urlpatterns = [
    path('history/', DepositHistoryView.as_view()),
    path('withdraw/', WithdrawView.as_view()),
    path('deposit/', DepositView.as_view()),
    path('balance/', UserBalanceView.as_view()),
    path('userassets/', UserAssetView.as_view()),
]
