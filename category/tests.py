from django.test import TestCase
from .models import Category
class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(
            Category_Options="Finance Bill",
            Daily_Updates="Sample update",
            Is_Active=True,
        )
        Category.objects.create(
            Category_Options="Bill of Rights",
            Daily_Updates="Another update",
            Is_Active=False,
        )
    def test_category_str_representation(self):
        category = Category.objects.get(Category_Options="Finance Bill")
        self.assertEqual(str(category), "Finance Bill")
    def test_category_count(self):
        count = Category.objects.count()
        self.assertEqual(count, 2)
    def test_active_categories(self):
        active_categories = Category.objects.filter(Is_Active=True)
        self.assertEqual(active_categories.count(), 1)
    def test_category_options_choices(self):
        category = Category.objects.get(Category_Options="Finance Bill")
        choices = dict(category._meta.get_field("Category_Options").choices)
        self.assertEqual(choices, {
            "Finance Bill": "Finance Bill",
            "Bill of Rights": "Bill of Rights"
        })
    def test_category_image_upload_path(self):
        category = Category.objects.get(Category_Options="Finance Bill")
        field = category._meta.get_field("Category_Image")
        upload_path = field.upload_to
        self.assertEqual(upload_path, "images/")