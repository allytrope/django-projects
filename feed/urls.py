from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('user/<str:username>/', views.user_page, name='user_page'),
    path('channel/<str:channel_name>/', views.feed, name='channel'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('new-post/<str:channel_name>/', views.new_post, name='new_post'),
    path('post-api/', views.post_api.as_view(), name='post_api'),
]