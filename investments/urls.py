from django.urls import path
from investments.views import InvestView

urlpatterns = [
    path("", InvestView.as_view(), name="invest"),
]
