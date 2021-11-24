from django.urls import path
from .views import PostDetail, PostSearch, PostListNews

urlpatterns = [
    path('', PostListNews.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path ('search', PostSearch.as_view()),
]