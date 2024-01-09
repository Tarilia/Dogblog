from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from dogblog.sitedog.models import Sitedog, TagPost
from django.views import View
from .forms import AddPostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .utils import DataMixin
from django.core.paginator import Paginator


class SitedogIndex(DataMixin, ListView):
    template_name = 'sitedog/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница'
    cat_selected = 0

    def get_queryset(self):
        return Sitedog.published.all().select_related('cat')


def about(request):
    return render(request, 'sitedog/about.html', {'title': 'О сайте'})


class ShowPost(DataMixin, DetailView):
    template_name = 'sitedog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Sitedog.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'sitedog/addpage.html'
    title_page = 'Добавление статьи'
    permission_required = 'sitedog.add_sitedog'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePage(PermissionRequiredMixin, DataMixin, UpdateView):
    model = Sitedog
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'sitedog/addpage.html'
    success_url = reverse_lazy('index')
    title_page = 'Редактирование статьи'
    permission_required = 'sitedog.change_sitedog'


def contact(request):
    return render(request, 'sitedog/contact.html', {'title': 'Обратная связь'})


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


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        post_slug = kwargs.get('slug')
        post = Sitedog.objects.get(id=post_slug)
        if post:
            post.delete()
        return redirect('index')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
