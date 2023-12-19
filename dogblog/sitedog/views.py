from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from dogblog.sitedog.models import Sitedog, Category


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


def index(request):
    posts = Sitedog.published.all()
    return render(request, 'sitedog/index.html', context={'title': 'Главная страница',
                                                          'menu': menu, 'posts': posts,
                                                           'cat_selected': 0, })


def about(request):
    return render(request, 'sitedog/about.html', context={'title': 'О сайте', 'menu': menu, })


def show_post(request, post_slug):
    post = get_object_or_404(Sitedog, slug=post_slug)
    return render(request, 'sitedog/post.html', context={'title': post.title, 'menu': menu,
                                                         'post': post, 'cat_selected': 1, })


def addpage(request):
    return HttpResponse(f'Добавление статьи')


def contact(request):
    return HttpResponse(f'Обратная связь')


def login(request):
    return HttpResponse(f'Авторизация')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Sitedog.published.filter(cat_id=category.pk)
    return render(request, 'sitedog/index.html', context={'title': f'Рубрика: {category.name}',
                                                          'menu': menu, 'posts': posts,
                                                          'cat_selected': category.pk, })


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
