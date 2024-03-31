# Register your models here.
from django.contrib import admin

from .models import Category, News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'content', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'id')
    list_editable = ['is_published', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
