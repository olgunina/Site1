# from admin import site
import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
#


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('News.urls')),
    path('human/', include('Human.urls')),
    path('register/', include('Register.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                path('__debug__/', include('debug_toolbar.urls')),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
