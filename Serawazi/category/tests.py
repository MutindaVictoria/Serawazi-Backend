from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Category

class CategoryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def create_category(self, options="Finance Bill", updates="Sample update", is_active=True):
        return Category.objects.create(Category_Options=options, Daily_Updates=updates, Is_Active=is_active)

    def test_create_category(self):
        data = {
            "Category_Options": "New Category",
            "Daily_Updates": "New update",
            "Is_Active": True,
        }
        response = self.client.post(reverse("category-list"), data, format="json")
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_categories(self):
        self.create_category()
        response = self.client.get(reverse("category-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_category_detail(self):
        category = self.create_category()
        response = self.client.get(reverse("category-detail", args=[category.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Category_Options"], category.Category_Options)

    
    def test_delete_category(self):
        category = self.create_category()
        response = self.client.delete(reverse("category-detail", args=[category.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=category.id).exists())

    def test_category_not_found(self):
        response = self.client.get(reverse("category-detail", args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
