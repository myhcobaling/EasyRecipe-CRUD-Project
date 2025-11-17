from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse_lazy


class HomepageView(TemplateView):
    template_name = 'app/home.html'


class AboutpageView(TemplateView):
    template_name = 'app/about.html'


class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog_list.html'



class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog_detail.html'


class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/blog_create.html'

    def get_form(self):
        form = super().get_form()
        form.fields['author'].queryset = User.objects.all()
        return form

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'app/blog_update.html'
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('blog')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('blog')



