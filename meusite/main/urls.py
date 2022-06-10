from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    # pagina index;
    # nome da lista na URL // <int:id> id da lista na url
    path("<int:id>", views.index, name="index"), 
    #home page
    path("1", views.home, name = 'home'),
    #pagina base 
    path("", views.base, name = 'base')
] 