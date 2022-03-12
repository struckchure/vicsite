from django.urls import path, include
from users.views import UserBalanceView, UserAssetView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('balance/', UserBalanceView.as_view()),
    path('userassets/', UserAssetView.as_view()),
]
