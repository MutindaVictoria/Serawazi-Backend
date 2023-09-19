from django.test import TestCase
from .models import Tutorial

# Create your tests here.

class TutorialModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tutorial.objects.create(
            introduction_texts='Introduction Texts',
            image='badge_images/test_image.jpg',
            description_texts='Test Description',
            gamified_elements='option1'
        )

    def test_introduction_texts_unique(self):
        tutorial = Tutorial.objects.get(id=1)
        unique = tutorial._meta.get_field('introduction_texts').unique
        self.assertTrue(unique)

    def test_image_upload_to(self):
        tutorial = Tutorial.objects.get(id=1)
        upload_to = tutorial._meta.get_field('image').upload_to
        self.assertEqual(upload_to, 'badge_images/')

    def test_gamified_elements_choices(self):
        tutorial = Tutorial.objects.get(id=1)
        choices = tutorial._meta.get_field('gamified_elements').choices
        self.assertEqual(choices, [('option1', 'Option 1'), ('option2', 'Option 2')])

    def test_str_representation(self):
        tutorial = Tutorial.objects.get(id=1)
        self.assertEqual(str(tutorial), tutorial.description_texts)

    def test_tutorial_instance(self):
        tutorial = Tutorial.objects.get(id=1)
        self.assertIsInstance(tutorial, Tutorial)

    # def test_description_texts_max_length(self):
    #     tutorial = Tutorial.objects.get(id=1)
    #     max_length = tutorial._meta.get_field('description_texts').max_length
    #     self.assertEqual(max_length, 255)
    #     self.assertLessEqual(max_length, 255)


    # def test_description_texts_blank(self):
    #     tutorial = Tutorial.objects.get(id=1)
    #     blank = tutorial._meta.get_field('description_texts').blank
    #     self.assertFalse(blank)

    # def test_description_texts_null(self):
    #     tutorial = Tutorial.objects.get(id=1)
    #     null = tutorial._meta.get_field('description_texts').null
    #     self.assertFalse(null)
        