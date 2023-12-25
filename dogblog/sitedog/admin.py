from django.contrib import admin, messages
from .models import Sitedog, Category
from django.utils.safestring import mark_safe


@admin.register(Sitedog)
class SitedogAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'tags']
    # exclude = ['tags', 'is_published']
    readonly_fields = ['post_photo']
    prepopulated_fields = {"slug": ("title", )}
    # filter_horizontal = ['tags']
    filter_vertical = ['tags']
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title', )
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = ['cat__name', 'is_published', 'tags']
    save_on_top = True

    @admin.display(description="Изображение", ordering='content')
    def post_photo(self, sitedog: Sitedog):
        if sitedog.photo:
            return mark_safe(f"<img src='{sitedog.photo.url}' width=50>")
        return "Без фото"

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Sitedog.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Sitedog.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
