from django.urls import path
from .views import test, stat

urlpatterns = [
    path("", test),
    path("page/", stat),
]