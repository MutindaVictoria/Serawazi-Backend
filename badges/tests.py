from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Badges


class BadgesModelTest(TestCase):
    
    def setUp(self):
        self.image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

    def test_create_badge(self):
        badge = Badges(
            name="Sample Badge",
            description="Description for the sample badge",
            image=self.image
        )

        badge.save()

        saved_badge = Badges.objects.get(pk=badge.pk)

        self.assertEqual(saved_badge.name, "Sample Badge")
        self.assertEqual(saved_badge.description, "Description for the sample badge")
        self.assertTrue(saved_badge.image.name.endswith(".jpg"))

    def test_badge_str(self):
        badge = Badges(
            name="Sample Badge",
            description="Description for the sample badge",
            image=self.image
        )

        self.assertEqual(str(badge), "Sample Badge")

    def test_name_unique(self):
        badge1 = Badges(
            name="Unique Badge",
            description="Description for unique badge",
            image=self.image
        )
        badge1.save()

        badge2 = Badges(
            name="Unique Badge",
            description="Description for another unique badge",
            image=self.image
        )

        with self.assertRaises(Exception):
            badge2.save()

    def test_description_blank(self):
        badge = Badges(
            name="Badge with Blank Description",
            description="",
            image=self.image
        )
        badge.save()

        saved_badge = Badges.objects.get(pk=badge.pk)
        self.assertEqual(saved_badge.description, "")

    def test_image_upload_to(self):
        badge = Badges(
            name="Image Upload Badge",
            description="Description for image upload badge",
            image=self.image
        )
        badge.save()

        saved_badge = Badges.objects.get(pk=badge.pk)
        self.assertTrue(saved_badge.image.name.startswith("badge_images/"))

   
