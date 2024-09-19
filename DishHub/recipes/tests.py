
from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    
    def setUp(self):
       
        self.recipe = Recipe.objects.create(
            recipe_id='1',
            title='Pasta',
            ingredients=['pasta', 'tomato sauce', 'cheese'],
            instructions='Boil pasta, add sauce, top with cheese.',
            image_url='http://example.com/image.jpg'
        )

    def test_recipe_instance_creation(self):
        
        self.assertEqual(self.recipe.recipe_id, '1')
        self.assertEqual(self.recipe.title, 'Pasta')
        self.assertEqual(self.recipe.ingredients, ['pasta', 'tomato sauce', 'cheese'])
        self.assertEqual(self.recipe.instructions, 'Boil pasta, add sauce, top with cheese.')
        self.assertEqual(self.recipe.image_url, 'http://example.com/image.jpg')

    def test_recipe_string_representation(self):
        
        self.assertEqual(str(self.recipe), 'Pasta')

    def test_empty_image_url(self):
        
        recipe_no_image = Recipe.objects.create(
            recipe_id='2',
            title='Salad',
            ingredients=['lettuce', 'tomato', 'cucumber'],
            instructions='Mix all ingredients together.',
            image_url=None  
        )
        self.assertIsNone(recipe_no_image.image_url)

    def test_invalid_recipe_id(self):

        with self.assertRaises(Exception):
            Recipe.objects.create(
                recipe_id='1',  
                title='Another Pasta',
                ingredients=['pasta', 'sauce'],
                instructions='Just cook it!',
                image_url='http://example.com/another.jpg'
            )

    def test_default_ingredients(self):
        
        recipe = Recipe.objects.create(
            recipe_id='4',
            title='Bread',
            instructions='Mix ingredients and bake.',
        )
        self.assertEqual(recipe.ingredients, [])

    def test_jsonfield_default(self):
        
        recipe_empty_ingredients = Recipe.objects.create(
            recipe_id='3',
            title='Soup',
            ingredients=[], 
            instructions='Heat water, add vegetables.',
        )
        self.assertEqual(recipe_empty_ingredients.ingredients, [])

if __name__ == '__main__':
    TestCase.main()