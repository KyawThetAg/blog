from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user_posts"),
    path('post/<str:pk>/', PostDetailView.as_view(), name="detail_post"),
    path('new/', PostCreateView.as_view(), name="create_post"),
    path('post/<str:pk>/update/', PostUpdateView.as_view(), name="update_post"),
    path('post/<str:pk>/delete/', PostDeleteView.as_view(), name="delete_post"),
    path('about/', views.about, name="blog-about"),
]
