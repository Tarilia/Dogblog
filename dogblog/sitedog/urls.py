from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('cats/<int:cats_id>/', views.categories),
    path('cats/<slug:cats_slug>/', views.categories_by_slug),
]
