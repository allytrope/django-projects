from django.shortcuts import render
from rest_framework import response, views

from .forms import PostForm
from .models import User, Channel, Post
from .serializers import PostSerializer

# Create your views here.
def feed(request, channel_name=None):
    posts = None
    current_channel = None
    if channel_name == None:
        posts = Post.objects.order_by('-date')
        channel_name = 'Unorganized'
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

def new_post(request, channel_name):
    channel = Channel.objects.get(name=channel_name)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    context = {
        'form': form,
        'channel': channel,
        }
    return render(request, 'feed/new_post.html', context)

class post_api(views.APIView):
    def get(self, request, *args, **kwargs):
        data = Post.objects.all()
        serializer = PostSerializer(data, many=True)
        return response.Response(serializer.data)

    #def post(self, request, *args, **kwargs):
    #    pass