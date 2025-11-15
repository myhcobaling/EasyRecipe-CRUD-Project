from django.shortcuts import render
from django.views.generic import TemplateView, ListView , DetailView
from django.views.generic.edit import CreateView
from .models import Post

class HomepageView(TemplateView):
    template_name = 'app/home.html'

class AboutpageView(TemplateView):
    template_name = 'app/about.html'

 class BlogListView(ListView):
     model = post
     context_object_name = 'posts'
    template_name = 'app/blog.html'


class BlogDetailView(DetailView):
    model = post
    context_object_name = 'posts'
template_name = 'app/blog.html'



