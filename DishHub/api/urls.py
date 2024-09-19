from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.CreateRecipeView.as_view(), name='create_recipe'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<str:recipe_id>/', views.FetchRecipeView.as_view(), name='fetch_recipe'),
    path('search/', views.SearchRecipeView.as_view(), name='search_recipe'),
]