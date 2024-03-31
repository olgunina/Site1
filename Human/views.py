from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

from Human.forms import HumanForm
from Human.utils import MyMixin
from .models import Human, Profession
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


# def register(request):
#    if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#        if form.is_valid():
#           form.save()
#          messages.success(request, 'Регистрация успешна')
#         return redirect('Login')
#    else:
#       messages.error(request, 'Ошибка регистрации')
#   else:
#      form = UserCreationForm()
#   return render(request, 'Human/register', {'form': form})


def login(request):
    return render(request, 'Human/login.html')


class HomeHuman(ListView, MyMixin):
    model = Human
    context_object_name = 'human'
    template_name = 'Human/home_human_list.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Human.objects.filter(is_published=True).select_related('profession')


class HumanByProfession(ListView, MyMixin):
    model = Human
    context_object_name = 'human'
    template_name = 'Human/home_human_list.html'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Human.objects.filter(profession_id=self.kwargs['profession_id'], is_published=True).select_related(
            'profession')


# def test(request):
#   objects = ['john', 'pol', 'tor', 'joy', 'nik', 'rik']
#  paginator = Paginator(objects, 2)
# page_num = request.Get.get('page', 1)
#  page_objects = paginator.get_page(page_num)
# return render(request, 'human/test.html', {'page_obj': page_objects})


class ViewHuman(DetailView):
    model = Human
    context_object_name = 'human_item'
    template_name = 'Human/view_human.html'


class AddHuman(CreateView):
    form_class = HumanForm
    template_name = 'Human/add_human.html'
    login_url = '/admin/'

# def index(request):
#  human = Human.objects.all()
#    professiones = Profession.objects.all()
#    context = {
#        'human': human,
#        'title': 'Биографии',
#    }
#    #    print(context)
#    return render(request, 'Human/Human.html', context=context)


# def get_profession(request, profession_id):
#    human = Human.objects.filter(profession_id=profession_id)
# #    professiones = Profession.objects.all()
#    profession = Profession.objects.get(pk=profession_id)
#    context = {
#        'human': human,
#        'profession': profession,
#    }
#    #    print(context)
#    return render(request, 'Human/profession.html', context=context)


# def view_human(request, human_id):
# #   human_item = Human.objects.get(pk=human_id)
#    human_item = get_object_or_404(Human, pk=human_id)
#    context = {
#        'human_item': human_item
#    }
#    return render(request, 'Human/view_human.html', context=context)


# def add_human(request):
#    if request.method == 'POST':
#        form = HumanForm(request.POST)
#        if form.is_valid():
#            # news = News.object.create(**form.cleaned_data)
#            human = form.save()
#            return redirect(human)
#    else:
#        form = HumanForm
#    return render(request, 'Human/add_human.html', {'form': form})
