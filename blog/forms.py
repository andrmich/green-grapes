from django import forms
from .models import Post
from hvad.forms import TranslatableModelForm


class PostForm(TranslatableModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body',)
