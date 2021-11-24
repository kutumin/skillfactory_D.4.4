from django.urls import path
from .views import PostDetail, PostSearch, PostListNews, PostAdd, ProductUpdateView

urlpatterns = [
    path('', PostListNews.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path ('search', PostSearch.as_view()),
    path ('add', PostAdd.as_view()),
    path('<int:pk>/edit', ProductUpdateView.as_view(), name='update_post_detail'),
]