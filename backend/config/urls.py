from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("backend.apps.accounts.urls")),
    path("",include("backend.apps.kitchen.urls"))
]
