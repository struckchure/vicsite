from django.urls import path, include

from accounts.views import (
    ProfileView,
    ProfileEdit,
    CustomPasswordChangeView,
)

urlpatterns = [
    
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/password_change/", CustomPasswordChangeView.as_view(), name="password_change"),
    path("profile/<int:pk>/edit/", ProfileEdit.as_view(), name="profile_edit"),

]
