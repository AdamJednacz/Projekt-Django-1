from django.urls import path
from .views import index,comment,like,unlike,about_us,contact

urlpatterns = [
    path('', index, name='home'),
    path('comments/', comment, name='comments'),
    path('like/', like, name='like'),
    path('unlike/', unlike, name='unlike'),
    path('about/', about_us, name='about'),
    path('contact/', contact, name='contact'),
]
