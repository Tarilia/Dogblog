from django.contrib import admin
from django.urls import path, include
from dogblog.sitedog.views import page_not_found


urlpatterns = [
    path('', include('dogblog.sitedog.urls')),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]


handler404 = page_not_found

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Породы собак"
