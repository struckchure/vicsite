from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from site_server.views import ChartView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("docs/", include_docs_urls(title="Avalog API")),
    path("invest/", include("investments.urls")),
    path("transactions/", include("transactions.urls")),
    path("contents/", include("contents.urls")),
    path("dashboard/charts/", ChartView.as_view(), name="charts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
