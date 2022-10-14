from django.urls import path
from . import views

app_name ='menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.menu_create, name='menu_create'),
    path('setDate/', views.setDate, name='setDate'),
    path('get_best_menu/', views.get_best_menu, name='get_best_menu'),
    path('vote/<int:menu_id>/', views.menu_vote, name='menu_vote'),
]
