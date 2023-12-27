from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from dogblog.sitedog.models import Sitedog, Category, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy


menu = [
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]


class SitedogIndex(ListView):
    template_name = 'sitedog/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Главная страница',
                     'menu': menu, 'cat_selected': 0, }

    def get_queryset(self):
        return Sitedog.published.all().select_related('cat')


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    return render(request, 'sitedog/about.html',
                  {'title': 'О сайте', 'menu': menu, 'form': form})


class ShowPost(DetailView):
    template_name = 'sitedog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['menu'] = menu
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Sitedog.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'sitedog/addpage.html'
    extra_context = {'menu': menu, 'title': 'Добавление статьи', }


def contact(request):
    return HttpResponse(f'Обратная связь')


def login(request):
    return HttpResponse(f'Авторизация')


class SitedogCategory(ListView):
    template_name = 'sitedog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Sitedog.published.filter(cat__slug=self.kwargs['cat_slug']).select_related("cat")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория - ' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context


class TagsPost(ListView):
    template_name = 'sitedog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Sitedog.published.filter(tags__slug=self.kwargs['tag_slug']).select_related("cat")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег - ' + tag.tag
        context['menu'] = menu
        context['cat_selected'] = None
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
