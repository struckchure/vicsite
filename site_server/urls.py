from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from site_server.views import ChartView, DashboardHomeView
from accounts.views import CustomSignupView, CustomLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/signup/", CustomSignupView.as_view(), name="signup"),
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path('accounts/', include('allauth.urls')),
    path("accounts/", include("accounts.urls")),
    path("invest/", include("investments.urls")),
    path("transactions/", include("transactions.urls")),
    path("contents/", include("contents.urls")),
    path("", DashboardHomeView.as_view(), name="home"),
    path("dashboard/charts/", ChartView.as_view(), name="charts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
