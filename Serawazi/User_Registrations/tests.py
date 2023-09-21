from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from .models import Roles, CustomUser

class CustomUserTest(TestCase):
    def setUp(self):
        self.role = Roles.objects.create(name='Test Role')
        self.group = Group.objects.create(name='Test Group')
        self.permission = Permission.objects.get(codename='add_customuser')  
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            phone_number='1234567890'
        )
        self.user.roles.add(self.role)
        self.user.groups.add(self.group)
        self.user.user_permissions.add(self.permission)

    def test_user_roles(self):
        self.assertEqual(self.user.roles.count(), 1)
        self.assertEqual(self.user.roles.first(), self.role)

    def test_user_groups(self):
        self.assertEqual(self.user.groups.count(), 1)
        self.assertEqual(self.user.groups.first(), self.group)

    def test_user_permissions(self):
        self.assertEqual(self.user.user_permissions.count(), 1)
        self.assertEqual(self.user.user_permissions.first(), self.permission)

    def test_user_email(self):
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_user_phone_number(self):
        self.assertEqual(self.user.phone_number, '1234567890')
