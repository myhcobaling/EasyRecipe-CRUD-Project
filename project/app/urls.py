from django.urls import path
from .views import (
    HomepageView, 
    AboutpageView, 
    RecipeListView, 
    RecipeDetailView, 
    RecipeCreateView, 
    RecipeUpdateView, 
    RecipeDeleteView
)

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
]