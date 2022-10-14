from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jjam/', include('jjam.urls')),
    path('menu/', include('menu.urls')),
    path('home/', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.index, name='index'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root = settings.MEDIA_ROOT)
