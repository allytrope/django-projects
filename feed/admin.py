from django.contrib import admin

from .models import User, Channel, Post, Comment

# Register your models here.
admin.site.register([User, Channel, Post, Comment])