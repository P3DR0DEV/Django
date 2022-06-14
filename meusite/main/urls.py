from urllib.parse import urlparse
from django.urls import path
from register import views as v
from . import views

urlpatterns = [
    # ToDoList
    # Nome da lista na URL // <int:id> id da lista na url
    path("<int:id>", views.index, name="index"),  
    #Home Page 
    path("home/", views.home, name = 'home'),
    path("create/", views.create , name="create"),
    path("", v.register, name="register")
] 