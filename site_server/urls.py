from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, reverse_lazy

from site_server.views import ChartView, DashboardHomeView, Custom_PasswordResetCompleteView, Custom_PasswordResetConfirmView, Custom_PasswordResetDoneView, Custom_PasswordResetView
from fronts.views import AboutPage, HomePageView
from accounts.views import SignupView, CustomLoginView


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("docs/", include_docs_urls(title="Avalog API")),
    # path('schema/', schema_view),

    path("accounts/signup/", SignupView, name="signup"),
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    # Password 
    path("password_reset/", Custom_PasswordResetView.as_view(), name="forgot_password"),
    path('password_reset/done/', Custom_PasswordResetDoneView.as_view(), name='c_password_reset_done'),
    path('password_reset/<uidb64>/<token>/', Custom_PasswordResetConfirmView.as_view(), name='c_password_reset_confirm'),
    path('password_reset/complete/', Custom_PasswordResetCompleteView.as_view(), name='c_password_reset_complete'),

    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("accounts.urls")),
    path("invest/", include("investments.urls")),
    path("transactions/", include("transactions.urls")),
    path("dashboard/", DashboardHomeView.as_view(), name="home"),
    path("dashboard/charts/", ChartView.as_view(), name="charts"),
    path("aboutus", AboutPage.as_view(), name="about_us"),
    path("", HomePageView.as_view(), name="homepage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
