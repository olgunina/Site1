from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView
# from Human.views import index, get_profession, view_human, add_human, test
from Human.views import HomeHuman, HumanByProfession, ViewHuman, AddHuman, login
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
#    path('', index, name='Home1'),
#    path('Profession/<int:profession_id>', get_profession, name='Profession'),
#    path('human/<int:human_id>', view_human, name='View_human'),
#    path('human/add_human', add_human, name='Add_human')
    path('', cache_page(30)(HomeHuman.as_view()), name='Home1'),
    path('Profession/<int:profession_id>', HumanByProfession.as_view(), name='Profession'),
    path('human/<int:pk>', ViewHuman.as_view(), name='View_human'),
    path('human/add_human', AddHuman.as_view(), name='Add_human'),
#    path('test/', test, name='Test'),
#    path('/register', register, name='Register'),
#    path('/login', login, name='Login'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

]
