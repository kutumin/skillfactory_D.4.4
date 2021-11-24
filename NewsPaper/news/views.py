from django.views.generic import ListView, DetailView
from .models import Post, PostCategory
from django.core.paginator import Paginator
from django.views import View 
from django.shortcuts import render
from .filters import PostFilter
from .forms import PostForm

class PostListNews(ListView):
    model = Post
    template_name = 'news.html' 
    context_object_name = 'news'
    queryset = Post.objects.filter(post_type='news')
    paginate_by = 1
    
class PostDetail(DetailView):
    model = Post
    template_name = 'details_news.html' 
    context_object_name = 'news'
    queryset = Post.objects.filter(post_type='news')

class PostSearch(ListView):
    model = Post
    template_name = 'search_news.html' 
    context_object_name = 'news'
    paginate_by = 1
    form_class = PostForm

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['PostCategory'] = PostCategory.objects.all()
        context['form'] = PostForm()
        return context
 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST) 
        
        if form.is_valid(): 
            form.save()
 
        return super().get(request, *args, **kwargs)
