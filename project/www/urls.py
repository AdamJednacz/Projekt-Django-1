from django.urls import path
from .views import index,comment,like,unlike

urlpatterns = [
    path('', index, name='home'),
    path('comments/', comment, name='comments'),
    path('likes/', like, name='like'),
    path('unlike/', unlike, name='unlike'),
]
