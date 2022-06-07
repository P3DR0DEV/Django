from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),  #nome da lista na URL // <int:id> id da lista na url
    path("", views.home, name = 'home')
] 