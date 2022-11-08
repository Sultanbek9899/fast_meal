from django.urls import path

from backend.apps.kitchen.views import index

urlpatterns = [
    path("", index,name="index")
]