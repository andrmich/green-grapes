from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post, Skill
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import translation
from django.shortcuts import render_to_response
from django.views.generic import TemplateView


class BlogListView(ListView):
    # user_languange = 'pl'
    # translation.activate(user_languange)
    # .sessiIon[translation.LANGUAGE_SESSION_KEY] = user_languange
    model = Post
    fields = '__all__'
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    fields = '__all__'
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class SkillListView(ListView):
    model = Skill
    template_name = 'skill.html'
    fields = '__all__'

class AboutPageView(TemplateView):
    template_name = "about.html"