from django.urls import path
from .views import (HomepageView, AboutpageView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, )


urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),


]