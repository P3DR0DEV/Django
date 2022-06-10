from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    # ToDoList
    # Nome da lista na URL // <int:id> id da lista na url
    path("<int:id>", views.index, name="index"),  
    #Home Page 
    path("", views.home, name = 'home')
] 