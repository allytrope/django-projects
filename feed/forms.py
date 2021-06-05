from django import forms

from .models import User, Channel, Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'content']