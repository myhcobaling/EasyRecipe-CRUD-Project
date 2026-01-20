from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Ingredient(models.Model):
    """Objective: Make it easy to search for recipes by ingredient """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    """Objective: Store basic recipe information (name, ingredients, steps) [cite: 12]"""
    title = models.CharField(max_length=200) # 
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    instructions = models.TextField() # [cite: 12]
    cooking_time = models.PositiveIntegerField(help_text="Time in minutes") # 
    # Relationships
    ingredients = models.ManyToManyField(Ingredient) # [cite: 12, 14]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})

class RecipeNotebook(models.Model):
    """Objective: Let users create a small recipe list or notebook [cite: 13]"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=100, default="My Recipes")
    recipes = models.ManyToManyField(Recipe) # [cite: 9]

    def __str__(self):
        return f"{self.user.username}'s {self.list_name}"