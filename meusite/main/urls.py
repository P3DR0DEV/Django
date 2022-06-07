from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
] 