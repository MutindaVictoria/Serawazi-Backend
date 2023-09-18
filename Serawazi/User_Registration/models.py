# from django.contrib.auth.models import AbstractUser, Permission, Group
# from django.db import models

# class CustomUser(AbstractUser):
#     groups = models.ManyToManyField(Group, related_name='customusers')
#     user_permissions = models.ManyToManyField(Permission, related_name='customusers')
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'password']

# class Admin(CustomUser):
#     age = models.PositiveIntegerField()
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#     ]

#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
#     achievements = models.TextField(default='', blank=True)

#     class Meta:
#         verbose_name_plural = "Admins"

# class RegularUser(CustomUser):
#     custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='related_regular_user')

#     user_permissions_related = models.ManyToManyField(
#     Permission,
#         verbose_name='user permissions',
#         blank=True,
#         related_name='regularuser_set',
#         related_query_name='regularuser'
#     )
#     class Meta:
#         verbose_name_plural = "Regular Users"
#     def set_default_customuser_ptr():
#         try:
#             return CustomUser.objects.first()
#         except CustomUser.DoesNotExist:
#             return None


from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):


    groups = models.ManyToManyField(
        Group,
        related_name='custom_users', 
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class Gamer(models.Model):
    user = models.CharField(max_length=255)
    # username = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    
  

class Admins(models.Model):
    user = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255, default="Unknown")









    
