from django import forms
from blog.models import Post
#from .models import Comment

'''class CommentForm(forms.ModelForm):
    class Meta:
        model       = Comment
        fields      = ('user', 'email', 'body')'''

class PostForm(forms.ModelForm):
    class Meta:
        model       = Post
        fields      = ('title', 'category', 'content', 'seo_title', 'seo_description', 'status')
