from django.urls import path
from . import views


urlpatterns = [
    path('', views.SitedogIndex.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.SitedogCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagsPost.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<slug:post_slug>/', views.ArticleFormDeleteView.as_view(), name='post_delete'),
]
