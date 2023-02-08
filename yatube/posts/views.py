from django.shortcuts import render
from django.http import HttpResponse

def index(request):    
    return HttpResponse('Главная страница')

def group_posts(request):
    return HttpResponse('Список сообществ')

def post_detail(request, slug):
    return HttpResponse(f'Название сообщества {slug}') 

