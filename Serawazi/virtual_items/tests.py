from django.test import TestCase
from .models import VirtualItem

class VirtualItemModelTest(TestCase):
    def setUp(self):
        # Create a sample VirtualItem
        self.virtual_item = VirtualItem.objects.create(
            name='Test Virtual Item',
            image='images/test_image.jpg'  # This path should be relative to your MEDIA_ROOT
        )

    def test_virtual_item_creation(self):
        virtual_item = VirtualItem.objects.get(name='Test Virtual Item')
        self.assertEqual(virtual_item.name, 'Test Virtual Item')
        self.assertEqual(virtual_item.image, 'images/test_image.jpg')  # Check the image path

    def test_virtual_item_str_representation(self):
        self.assertEqual(str(self.virtual_item), 'Test Virtual Item')
