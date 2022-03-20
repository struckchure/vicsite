from django.urls import path, include
from accounts.views import UserBalanceView, UserAssetView, UserAsset, CoinAddressView, CoinOptionView

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("balance/", UserBalanceView.as_view()),
    path("userassets/", UserAsset.as_view()),
    path("userassets/edit/", UserAssetView.as_view()),
    path("coins/", CoinOptionView.as_view()),
    path("coinaddress/<int:coin_id>/", CoinAddressView.as_view()),
]
