from django.db.models import Count, F

from Human.models import Profession
from django import template
from django.core.cache import cache

register = template.Library()


@register.simple_tag(name='get_list_professiones')
def get_list_professiones():
    return Profession.objects.all()


@register.inclusion_tag('Human/list_professiones.html')
def show_professiones(arg1='Список ', arg2='знаменитостей'):
    #     professiones = Profession.objects.all()
    #      professiones = Profession.objects.annotate(cnt=Count('human', filter=F('human__is_published'))).filter(cnt__gt=0)
    professiones = cache.get('professiones')
    if not professiones:
        professiones = Profession.objects.annotate(cnt=Count('Human', filter=F('human__is_published'))).filter(
            cnt__gt=0)
        cache.set('professiones', professiones, 60)
    return {'professiones': professiones, 'arg1': arg1, 'arg2': arg2}
