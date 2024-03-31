from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Human, Profession
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class HumanAdminForm(forms.ModelForm):
    biografia = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Human
        fields = '__all__'


class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_surname', 'profession', 'biografia', 'get_photo', 'is_published')
    list_display_links = ('id', 'name_surname')
    search_fields = ('profession', 'is_published')
    list_filter = ('is_published', 'id')
    list_editable = ['is_published', 'profession']
    fields = ('name_surname', 'biografia', 'get_photo', 'is_published', 'birthdate')
    readonly_fields = ('get_photo', 'updated_at')
    form = HumanAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото нет'

    get_photo_description = 'Миниатюра'


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'biografia')


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'
