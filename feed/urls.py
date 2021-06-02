from django.urls import path

from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('user/<str:username>/', views.user_page, name='user_page'),
    path('channel/<str:channel_name>/', views.feed, name='channel'),
    path('post/<int:post_id>/', views.post, name='post'),
]