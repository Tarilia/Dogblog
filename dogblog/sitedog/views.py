from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Страница приложения</h1>')


def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')


def categories(request, cats_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cats_id}</p>')


def categories_by_slug(request, cats_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cats_slug}</p>')
