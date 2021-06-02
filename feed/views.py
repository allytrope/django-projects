from django.shortcuts import render

from .models import User, Channel, Post

# Create your views here.
def feed(request, channel_name=None):
    posts = None
    current_channel = None
    if channel_name == None:
        posts = Post.objects.order_by('-date')
    else:
        posts = Post.objects.filter(channel=channel_name).order_by('-date')
        current_channel = Channel.objects.get(name=channel_name)
    channels = Channel.objects.all()
    context = {
        'posts': posts,
        'channels': channels,
        'current_channel': current_channel,
        }
    return render(request, 'feed/feed.html', context)

def user_page(request, username):
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'feed/user_page.html', context)

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post': post}
    return render(request, 'feed/post.html', context)