from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('docs/', include_docs_urls(title="Avalog API")),
    path('investments/', include('investments.urls')),
    path('transactions/', include('transactions.urls')),
]
