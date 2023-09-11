# from django.test import TestCase
# from .models import ScenarioCollection
# from django.core.exceptions import ValidationError

# class ScenarioCollectionModelTest(TestCase):
#     def setUp(self):
#         # Create a sample ScenarioCollection instance for testing
#         self.collection = ScenarioCollection.objects.create(
#             name='Test Collection',
#             description='Test Description',
#             cover_Image='path/to/test/image.jpg',
#             total_Scenarios=5,
#         )

#     def test_str_representation(self):
#         # Test the __str__ method of the ScenarioCollection model
#         self.assertEqual(str(self.collection), 'Test Collection')

#     def test_fields(self):
#         # Test individual fields of the ScenarioCollection model
#         self.assertEqual(self.collection.name, 'Test Collection')
#         self.assertEqual(self.collection.description, 'Test Description')
#         self.assertEqual(self.collection.cover_Image, 'path/to/test/image.jpg')
#         self.assertEqual(self.collection.total_Scenarios, 5)

#     def test_negative_total_scenarios(self):
#         # Test that a ScenarioCollection instance with a negative Total_Scenarios value is not allowed
#         with self.assertRaises(ValidationError):
#             ScenarioCollection.objects.create(
#                 name='Invalid Collection',
#                 description='Invalid Description',
#                 cover_Image='path/to/invalid/image.jpg',
#                 total_Scenarios=-1,
#             )
