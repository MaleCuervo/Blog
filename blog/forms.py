from django import forms
from .models import Post, Comment

#form to add post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

#form add coment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)