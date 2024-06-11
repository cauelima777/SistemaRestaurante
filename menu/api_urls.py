from django.urls import path
from . import api

urlpatterns = [
    path('menu/', api.api_menu_list, name='api_menu_list'),
    path('menu/create/', api.api_menu_create, name='api_menu_create'),
    path('menu/update/<int:item_id>/', api.api_menu_update, name='api_menu_update'),
    path('menu/delete/<int:item_id>/', api.api_menu_delete, name='api_menu_delete'),
]
