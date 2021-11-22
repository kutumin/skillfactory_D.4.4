from django.urls import path
from .views import PostList,PostDetail, PostSearch

urlpatterns = [
    path('', PostSearch.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path ('search', PostList.as_view()),
]