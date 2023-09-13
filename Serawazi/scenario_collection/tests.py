from django.test import TestCase
from .models import ScenarioCollection

class ScenarioCollectionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ScenarioCollection.objects.create(
            name='Test Collection',
            description='This is a test collection',
            cover_Image='covers/test.jpg',
            total_Scenarios=10
        )

    def test_name_max_length(self):
        collection = ScenarioCollection.objects.get(id=1)
        max_length = collection._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_description_field(self):
        collection = ScenarioCollection.objects.get(id=1)
        self.assertEquals(collection.description, 'This is a test collection')

    def test_cover_image_upload_to(self):
        collection = ScenarioCollection.objects.get(id=1)
        self.assertEquals(collection.cover_Image, 'covers/test.jpg')

    def test_total_scenarios_positive_integer(self):
        collection = ScenarioCollection.objects.get(id=1)
        self.assertTrue(collection.total_Scenarios >= 0)

    def test_object_name(self):
        collection = ScenarioCollection.objects.get(id=1)
        expected_object_name = collection.name
        self.assertEquals(str(collection), expected_object_name)
