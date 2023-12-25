from django.urls import path
from . import views


urlpatterns = [
    path('', views.SitedogIndex.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.SitedogCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagsPost.as_view(), name='tag'),
]
