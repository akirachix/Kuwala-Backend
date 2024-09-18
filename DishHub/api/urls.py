from django.urls import path
from .views import CreateRecipeView, RecipeListView, FetchRecipeView, SearchRecipeView

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),  
    path('recipes/create/', CreateRecipeView.as_view(), name='create_recipe'),
    path('recipes/<int:recipe_id>/', FetchRecipeView.as_view(), name='fetch_recipe'),  
    path('recipes/search/', SearchRecipeView.as_view(), name='search_recipes'),  
]