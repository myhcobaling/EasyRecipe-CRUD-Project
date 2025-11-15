from django.urls import path
from .views import HomepageView, AboutpageView, BlogListView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blog'),
]