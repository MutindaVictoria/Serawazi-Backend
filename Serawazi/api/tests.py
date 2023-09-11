# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from scenario_collection.models import ScenarioCollection
# from .serializers import ScenarioCollectionSerializer

# class ScenarioCollectionAPITest(TestCase):
#     def setUp(self):
#         # Create a sample ScenarioCollection instance for testing
#         self.collection = ScenarioCollection.objects.create(
#             name='Test Collection',
#             description='Test Description',
#             cover_Image='path/to/test/image.jpg',
#             total_Scenarios=5,
#         )
#         self.client = APIClient()

#     def test_list_collections(self):
#         # Test the API endpoint to list all ScenarioCollections
#         url = reverse('collection-list')
#         response = self.client.get(url)
#         collections = ScenarioCollection.objects.all()
#         serializer = ScenarioCollectionSerializer(collections, many=True)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)

#     def test_retrieve_collection(self):
#         # Test the API endpoint to retrieve a specific ScenarioCollection
#         url = reverse('collection-detail', kwargs={'pk': self.collection.id})
#         response = self.client.get(url)
#         collection = ScenarioCollection.objects.get(pk=self.collection.id)
#         serializer = ScenarioCollectionSerializer(collection)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)

#     def test_create_collection(self):
#         # Test the API endpoint to create a new ScenarioCollection
#         url = reverse('collection-list')
#         data = {
#             'name': 'New Collection',
#             'description': 'New Description',
#             'cover_Image': 'path/to/new/image.jpg',
#             'total_Scenarios': 10,
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_update_collection(self):
#         # Test the API endpoint to update an existing ScenarioCollection
#         url = reverse('collection-detail', kwargs={'pk': self.collection.id})
#         data = {
#             'name': 'Updated Collection',
#             'description': 'Updated Description',
#             'cover_Image': 'path/to/updated/image.jpg',
#             'total_Scenarios': 15,
#         }
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_delete_collection(self):
#         # Test the API endpoint to delete a ScenarioCollection
#         url = reverse('collection-detail', kwargs={'pk': self.collection.id})
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
