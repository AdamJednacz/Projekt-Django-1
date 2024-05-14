from django.contrib import admin
from .models import User,Comment,Like

# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Like)