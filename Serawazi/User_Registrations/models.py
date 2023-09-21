from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

class Roles(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission, related_name='roles')
    

class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=100)
    roles = models.ManyToManyField(Roles, related_name='users')
    email = models.EmailField(max_length=23)
    
    
    custom_groups = models.ManyToManyField(Group, related_name='custom_users')
    custom_user_permissions = models.ManyToManyField(
        Permission, related_name='custom_users_permissions'
    )