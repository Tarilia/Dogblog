from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


menu = [
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Кавказская овчарка', 'content': 'Описание породы', 'is_published': True},
    {'id': 2, 'title': 'Немецкий дог', 'content': 'Описание породы', 'is_published': True},
    {'id': 3, 'title': 'Ротвейлер', 'content': 'Описание породы', 'is_published': False},
]


cats_db = [
    {'id': 1, 'name': 'Служебная'},
    {'id': 2, 'name': 'Охранная'},
    {'id': 3, 'name': 'Декоративная'},
]


def index(request):
    return render(request, 'sitedog/index.html', context={'title': 'Главная страница',
                                                          'menu': menu, 'posts': data_db,
                                                           'cat_selected': 0, })


def about(request):
    return render(request, 'sitedog/about.html', context={'title': 'О сайте', 'menu': menu, })


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи id: {post_id}')


def addpage(request):
    return HttpResponse(f'Добавление статьи')


def contact(request):
    return HttpResponse(f'Обратная связь')


def login(request):
    return HttpResponse(f'Авторизация')


def show_category(request, cat_id):
    return render(request, 'sitedog/index.html', context={'title': 'Отображение по рубрикам',
                                                          'menu': menu, 'posts': data_db,
                                                          'cat_selected': cat_id, })


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
