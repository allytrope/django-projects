from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField()
    avatar = models.ImageField(blank=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('user_page', kwargs={'username': self.username})

class Channel(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('channel', kwargs={'channel_name': self.name})

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + ' follows ' + self.channel

    class Meta:
        unique_together = ['user', 'channel']

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post', kwargs={'post_id': self.pk})

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.content

class Sentiment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    sentiment = models.BooleanField()  # True, False = Upvote, Downvote
 
    def __str__(self):
        if self.sentiment == True:
            return self.user + 'liked' + self.post.title
        else:
            return self.user + 'disliked' + self.post.title

    class Meta:
        unique_together = ['user', 'post']