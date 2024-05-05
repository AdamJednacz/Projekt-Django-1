from django.urls import path
from .views import index,comment

urlpatterns = [
    path('', index, name='home'),
    path('comments/', comment, name='comments'),
]
