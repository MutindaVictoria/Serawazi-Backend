# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import Category

# class CategoryTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.category_data = {
#             'Category_Options': 'option1',
#             'Daily_Updates': 'Some daily updates',
#             'Category_Image': None,  
#             'Is_Active': True,
#         }
#         self.category = Category.objects.create(**self.category_data)

#     def test_create_category(self):
#         response = self.client.post('/categories/', self.category_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_read_category(self):
#         response = self.client.get(f'/categories/{self.category.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_category(self):
#         updated_data = {
#             'Category_Options': 'option2',
#             'Daily_Updates': 'Updated daily updates',
#             'Is_Active': False,
#         }
#         response = self.client.put(f'/categories/{self.category.id}/', updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.category.refresh_from_db()
#         self.assertEqual(self.category.Category_Options, updated_data['Category_Options'])

#     def test_delete_category(self):
#         response = self.client.delete(f'/categories/{self.category.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
