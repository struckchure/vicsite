from django.urls import path, include
from accounts.views import (
    ContactView,
    CustomSignupView,

)

urlpatterns = [
    path("contactus/", ContactView.as_view()),
    path("signup/", CustomSignupView.as_view(), name="signup"),
]
