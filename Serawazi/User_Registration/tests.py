from django.test import TestCase
from .models import User_Registration

class UserRegistrationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User_Registration.objects.create(
            first_name="zelani",
            last_name="zelani",
            email="zelani@gmail.com",
            password="password",
            username="zelanizelani"
        )

    def test_first_name_max_length(self):
        user = User_Registration.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 255)

    def test_last_name_max_length(self):
        user = User_Registration.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 255)

    def test_email(self):
        user = User_Registration.objects.get(id=1)
        self.assertEquals(user.email, "zelani@gmail.com")

    def test_password_max_length(self):
        user = User_Registration.objects.get(id=1)
        max_length = user._meta.get_field('password').max_length
        self.assertEquals(max_length, 255)

    def test_username_max_length(self):
        user = User_Registration.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 255)

    def test_str_representation(self):
        user = User_Registration.objects.get(id=1)
        expected_str = f"{user.first_name} {user.last_name}"
        self.assertEqual(str(user), expected_str)
