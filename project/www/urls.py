from django.urls import path
from .views import index,comment,like_comment,unlike_comment

urlpatterns = [
    path('', index, name='home'),
    path('comments/', comment, name='comments'),
    path('like_comment/',like_comment, name='like_comment'),
    path('unlike_comment/',unlike_comment, name='unlike_comment'),
]
