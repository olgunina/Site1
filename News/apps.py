from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'News'
    verbose_name = 'Новости'

# class CategoryConfig(AppConfig):
#    default_auto_field = 'django.db.models.BigAutoField'
#     name = 'Category'
#    verbose_name = 'Категории'
