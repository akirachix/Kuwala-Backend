# from django.shortcuts import render
# # Create your views here.
# from rest_framework import status
# from rest_framework.response import Response
# from .models import Recipe
# from rest_framework.views import APIView
# from .serializers import RecipeSerializer

# class RecipeListView(APIView):
#     def get(self, request):
#         recipe= Recipe.objects.all()
#         serializer = RecipeSerializer(recipe, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = RecipeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class RecipeDetailView(APIView):
#     def get(self, request, recipe_id):
#         recipe = self.get_object(recipe_id)
#         serializer = RecipeSerializer(recipe)
#         return Response(serializer.data)
#     def put(self, request, recipe_id):
#         recipe = self.get_object(recipe_id)
#         serializer = RecipeSerializer(recipe, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, recipe_id):
#         recipe = self.get_object(recipe_id)
#         recipe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     def post(self, request, recipe_id):
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#     def get_object(self, recipe_id):
#         from django.shortcuts import get_object_or_404
#         return get_object_or_404(Recipe, pk=recipe_id)