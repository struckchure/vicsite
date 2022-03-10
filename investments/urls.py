from django.urls import path
from investments.views import InvestView

urlpatterns = [
    path('invest/', InvestView.as_view()),
]
