from django.urls import path, include
from accounts.views import (
    ContactView,

)

urlpatterns = [
    path("contactus/", ContactView.as_view()),
]
