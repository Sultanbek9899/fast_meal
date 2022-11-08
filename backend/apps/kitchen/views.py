from curses.ascii import HT
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1> Главная страница </h1>")


    

