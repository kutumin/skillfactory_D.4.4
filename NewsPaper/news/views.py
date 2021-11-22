from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator
from django.views import View 
from django.shortcuts import render
from .filters import PostFilter

class PostList(ListView):
    model = Post
    template_name = 'news.html' 
    context_object_name = 'news'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'details_news.html' 
    context_object_name = 'news'
    queryset = Post.objects.filter(post_type='news')

class PostSearch(ListView):
    model = Post
    template_name = 'search_news.html' 
    context_object_name = 'news'
    queryset = Post.objects.filter(post_type='news')
    paginate_by = 1
