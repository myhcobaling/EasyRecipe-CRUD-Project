from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Recipe  # Changed from Book
from django.urls import reverse_lazy

class HomepageView(TemplateView):
    template_name = 'app/home.html'

class AboutpageView(TemplateView):
    template_name = 'app/about.html'

class RecipeListView(ListView): # Changed name
    model = Recipe                    
    context_object_name = 'recipes'    
    template_name = 'app/recipe_list.html'

class RecipeDetailView(DetailView): # Changed name
    model = Recipe
    context_object_name = 'recipe'    
    template_name = 'app/recipe_detail.html'

class RecipeCreateView(CreateView): # Changed name
    model = Recipe
    # Updated fields to match your Proposal objectives 
    fields = ['title', 'ingredients', 'instructions', 'cooking_time'] 
    template_name = 'app/recipe_create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(UpdateView): # Changed name
    model = Recipe
    template_name = 'app/recipe_update.html'
    fields = ['title', 'ingredients', 'instructions', 'cooking_time'] 
    success_url = reverse_lazy('recipe_list')  

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'app/recipe_delete.html'
    success_url = reverse_lazy('recipe_list') # Redirects back to the list
