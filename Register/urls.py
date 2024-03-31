from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView
# from Human.views import index, get_profession, view_human, add_human, test
from Register.views import register, user_logout, user_login

urlpatterns = [
     path('register/', register, name='Register'),
#     path('__debug__/', include('debug_toolbar.urls')),
     path('login/', user_login, name='Login'),
     path('logout/', user_logout, name='Logout'),
     path('__debug__/', include('debug_toolbar.urls')),
]
