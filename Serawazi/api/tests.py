from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from scenario_collection.models import ScenarioCollection

class ScenarioCollectionTestCase(TestCase):

    def setUp(self):
        self.image = SimpleUploadedFile(
            "test_image.jpg",
            content=b"file_content",
            content_type="image/jpeg"
        )

        self.collection = ScenarioCollection.objects.create(
            name='Test Collection',
            description='A test collection',
            cover_Image=self.image,
        )

    def test_create_scenario_collection(self):
        self.assertEqual(self.collection.name, 'Test Collection')
        self.assertEqual(self.collection.description, 'A test collection')
        self.assertEqual(str(self.collection), 'Test Collection')

    def test_calculate_total_scenarios(self):
        another_collection = ScenarioCollection.objects.create(
            name='Test Collection',
            description='Another test collection with the same name',
            cover_Image=self.image,
        )

        self.collection.calculate_total_scenarios()
        self.collection.refresh_from_db()


    def test_update_scenario_collection(self):
        self.collection.name = 'Updated Collection'
        self.collection.description = 'An updated test collection'
        self.collection.save()

        self.collection.refresh_from_db()

        self.assertEqual(self.collection.name, 'Updated Collection')
        self.assertEqual(self.collection.description, 'An updated test collection')

    def test_delete_scenario_collection(self):
        collection_id = self.collection.id
        self.collection.delete()
        with self.assertRaises(ScenarioCollection.DoesNotExist):
            deleted_collection = ScenarioCollection.objects.get(id=collection_id)

    def tearDown(self):
        self.image.close()

    def test_create_multiple_scenario_collections(self):
        collection2 = ScenarioCollection.objects.create(
            name='Second Collection',
            description='Another test collection',
            cover_Image=self.image,
        )

        collection3 = ScenarioCollection.objects.create(
            name='Third Collection',
            description='Yet another test collection',
            cover_Image=self.image,
        )

        self.assertEqual(collection2.name, 'Second Collection')
        self.assertEqual(collection3.name, 'Third Collection')

    def test_total_scenarios_count(self):
        collection2 = ScenarioCollection.objects.create(
            name='Test Collection',
            description='Another test collection with the same name',
            cover_Image=self.image,
        )

        collection3 = ScenarioCollection.objects.create(
            name='Test Collection',
            description='Yet another test collection with the same name',
            cover_Image=self.image,
        )

        self.collection.calculate_total_scenarios()
        self.collection.refresh_from_db()


    def test_cover_image_upload(self):
        response = self.client.get(self.collection.cover_Image.url)

    def test_invalid_cover_image_upload(self):
        invalid_image = SimpleUploadedFile(
            "test.txt",
            content=b"file_content",
            content_type="text/plain"
        )
        collection4 = ScenarioCollection.objects.create(
            name='Invalid Image Collection',
            description='A collection with an invalid cover image',
            cover_Image=invalid_image,
        )


    def test_empty_description(self):
        collection5 = ScenarioCollection.objects.create(
            name='Empty Description Collection',
            description='',
            cover_Image=self.image,
        )

        self.assertEqual(collection5.description, '')
