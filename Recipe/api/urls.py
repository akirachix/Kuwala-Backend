# from django.urls import path,include
from django.urls import path
from .views import RecipeListView,RecipeDetailView

# urlpatterns=[
#     path('recipe/' , include('recipe.urls')),
# ]
urlpatterns = [
    path("recipe/", RecipeListView.as_view(), name="recipe_list_view"),
    path("recipe/<int:id>/",RecipeDetailView.as_view(),name="recipe_detail_view")
]