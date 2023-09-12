# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import VirtualItem

# class VirtualItemTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.virtual_item_data = {'name': 'Iconic Item', 'image': 'Iconic.jpg'}

#     def test_api_can_create_virtual_item(self):
#         response = self.client.post('/virtual-items/', self.virtual_item_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_api_can_get_virtual_item(self):
#         virtual_item = VirtualItem.objects.create(**self.virtual_item_data)
#         response = self.client.get(f'/virtual-items/{virtual_item.id}/', format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, virtual_item.name)
