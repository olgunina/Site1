from django.db import models
from django.urls import reverse_lazy


class Profession(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('profession', kwargs={'profession_id': self.pk})

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['title']


class Human(models.Model):
    name_surname = models.CharField(max_length=150, verbose_name='Кто это')
    biografia = models.TextField(blank=True, verbose_name='Биография')
    birthdate = models.DateTimeField(help_text='birthdate', verbose_name='Дата рождения')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Дата публикации')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('View_human', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Знаменитость'
        verbose_name_plural = 'Знаменитости'
        ordering = ['-is_published']
