
from rest_framework import generics
from django.http import JsonResponse
import requests
from recipes.models import Recipe
from .serializers import RecipeSerializer, RecipeListSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateRecipeView(APIView):
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Recipe created successfully'}, status=201)
        return Response(serializer.errors, status=400)

class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer

class FetchRecipeView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'recipe_id'

class SearchRecipeView(generics.GenericAPIView):
    def get(self, request):
        query = request.GET.get('q', '')
        search_type = request.GET.get('type', 'name')
        
        if not query:
            return JsonResponse({'error': 'Please provide a search query'}, status=400)

        if search_type == 'ingredients':
            return self.search_by_ingredients(query)
        else:
            return self.search_by_name(query)
    
    def search_by_ingredients(self, query):
        ingredients = [ingredient.strip() for ingredient in query.split(',')]
        
        all_recipes = []
        for ingredient in ingredients:
            url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
            response = requests.get(url)

            if response.status_code != 200:
                return JsonResponse({'error': f'Could not fetch recipes from MealDB for ingredient: {ingredient}'}, status=500)

            data = response.json()
            if 'meals' in data and data['meals']:
                all_recipes.extend(data['meals'])

        if all_recipes:
            unique_recipes = {meal['idMeal']: meal for meal in all_recipes}.values()
            detailed_recipes = [self.get_or_create_recipe(meal['idMeal']) for meal in unique_recipes]
            detailed_recipes = [RecipeSerializer(recipe).data for recipe in detailed_recipes if recipe]

            return JsonResponse({'recipes': detailed_recipes}, status=200)

        return JsonResponse({'message': 'No recipes found for the given ingredients'}, status=404)

    def search_by_name(self, query):
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
        response = requests.get(url)

        if response.status_code != 200:
            return JsonResponse({'error': 'Could not fetch recipes from MealDB'}, status=500)

        data = response.json()
        if 'meals' in data and data['meals']:
            detailed_recipes = [self.get_or_create_recipe(meal['idMeal']) for meal in data['meals']]
            detailed_recipes = [RecipeSerializer(recipe).data for recipe in detailed_recipes if recipe]
            return JsonResponse({'recipes': detailed_recipes}, status=200)

        return JsonResponse({'message': 'No recipes found for the given query'}, status=404)

    def get_or_create_recipe(self, recipe_id):
        try:
            return Recipe.objects.get(recipe_id=recipe_id)
        except Recipe.DoesNotExist:
            recipe_data = self.fetch_recipe_from_api(recipe_id)
            if recipe_data:
                return Recipe.objects.create(**recipe_data)
        return None

    def fetch_recipe_from_api(self, recipe_id):
        url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={recipe_id}"
        response = requests.get(url)

        if response.status_code != 200:
            return None
        
        data = response.json()
        
        if 'meals' in data and data['meals']:
            meal = data['meals'][0]
            ingredients = [f"{meal.get(f'strMeasure{i}') or ''} {meal.get(f'strIngredient{i}') or ''}".strip()
                           for i in range(1, 21) if meal.get(f'strIngredient{i}')]

            return {
                'recipe_id': meal['idMeal'],
                'title': meal['strMeal'],
                'ingredients': ingredients,
                'instructions': meal['strInstructions'],
                'image_url': meal['strMealThumb']
            }
        
        return None