from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from dogblog.sitedog.models import Sitedog, Category, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView
from django.urls import reverse_lazy
from .utils import DataMixin


menu = [
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]


class SitedogIndex(DataMixin, ListView):
    template_name = 'sitedog/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница'
    cat_selected = 0

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


class ShowPost(DataMixin, DetailView):
    template_name = 'sitedog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Sitedog.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'sitedog/addpage.html'
    title_page = 'Добавление статьи'


class UpdatePage(DataMixin, UpdateView):
    model = Sitedog
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'sitedog/addpage.html'
    success_url = reverse_lazy('index')
    title_page = 'Редактирование статьи'


def contact(request):
    return HttpResponse(f'Обратная связь')


def login(request):
    return HttpResponse(f'Авторизация')


class SitedogCategory(DataMixin, ListView):
    template_name = 'sitedog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Sitedog.published.filter(cat__slug=self.kwargs['cat_slug']).select_related("cat")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context, title='Категория - ' + cat.name,
                                      cat_selected=cat.pk, )


class TagsPost(DataMixin, ListView):
    template_name = 'sitedog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Sitedog.published.filter(tags__slug=self.kwargs['tag_slug']).select_related("cat")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Тег: ' + tag.tag)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
