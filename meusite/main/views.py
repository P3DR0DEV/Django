from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList

# Create your views here.

#pagina ToDoList
def index(response, id):
    ls = ToDoList.objects.get(id= id) #Adiciona o nome da lista
    #item = ls.item_set.get(id=1) #Adiciona os itens da lista
    return render(response, "main/list.html", {"ls": ls})

#home page
def home(response):
    return render(response, "main/home.html", {})

#pagina base
def base(response):
    return render(response,"main/base.html", {})
