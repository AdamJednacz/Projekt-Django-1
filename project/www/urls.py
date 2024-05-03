from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brand/', views.Brand_List, name='brand-list'),
    path('model/', views.Model_List, name='model-list'),
    path('user/', views.User_List, name='user-list'),
    path('add_brand/', views.add_Brand, name='add-brand'),
    path('add_model/', views.add_Model, name='add-model'),
    path('add_user/', views.add_User, name='add-user'),
    path('zapisano/', views.zapisano, name='zapisano'),
]