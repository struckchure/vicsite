from django.urls import path, include
from allauth.account.views import confirm_email
from users.views import UserBalanceView, UserAssetView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    path('account/registration/account-confirm-email/<int:pk>/', confirm_email, name='account_confirm_email'),
    path('balance/', UserBalanceView.as_view()),
    path('userassets/', UserAssetView.as_view()),
]
