from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from dogblog.sitedog.models import Sitedog, Category, TagPost
from .forms import AddPostForm


menu = [
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]


def index(request):
    posts = Sitedog.published.all().select_related('cat')
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
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Sitedog.objects.create(**form.cleaned_data)
                return redirect('index')
            except:
                form.add_error(None, "Ошибка добавления поста")
    else:
        form = AddPostForm()
    return render(request, 'sitedog/addpage.html', context={'menu': menu, 'title': 'Добавление статьи',
                                                            'form': form, })


def contact(request):
    return HttpResponse(f'Обратная связь')


def login(request):
    return HttpResponse(f'Авторизация')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Sitedog.published.filter(cat_id=category.pk).select_related('cat')
    return render(request, 'sitedog/index.html', context={'title': f'Рубрика: {category.name}',
                                                          'menu': menu, 'posts': posts,
                                                          'cat_selected': category.pk, })

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Sitedog.Status.PUBLISHED).select_related('cat')
    return render(request, 'sitedog/index.html', context={'title': f"Тег: {tag.tag}", 'menu': menu,
                                                        'posts': posts, 'cat_selected': None, })


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
