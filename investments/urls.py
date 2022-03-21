from django.urls import path
from investments.views import InvestView, PackageView, InvestHistoryView

urlpatterns = [
    path("invest/", InvestView.as_view()),
    path("history/", InvestHistoryView.as_view()),
    path("packages/", PackageView.as_view()),
]
