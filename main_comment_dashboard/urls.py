from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),

    path('list-unitname/', list_unitname, name='list-unitname'),
    path('delete-unitname/', delete_unitname, name='delete-unitname'),
    path('create-unitname/', create_unitname, name='create-unitname'),
    path('update-unitname/', update_unitname, name='update-unitname'),

    path('get-unit-names/', get_unit_names, name='get-unit-names'),
    path('list-unitname-address/', list_unitname_address, name='list-unitname-address'),
    path('delete-unitname-address/', delete_unitname_address, name='delete-unitname-address'),
    path('create-unitname-address/', create_unitname_address, name='create-unitname-address'),
    path('update-unitname-address/', update_unitname_address, name='update-unitname-address'),

    path('list-unitname-address-comment/', list_unitname_address_comment, name='list-unitname-address-comment'),
    path('delete-unitname-address-comment/', delete_unitname_address_comment, name='delete-unitname-address-comment'),
    path('create-unitname-address-comment/', create_unitname_address_comment, name='create-unitname-address-comment'),
    path('update-unitname-address-comment/', update_unitname_address_comment, name='update-unitname-address-comment'),



]
