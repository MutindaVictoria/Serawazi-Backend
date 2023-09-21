from django.contrib.auth.models import Permission
from User_Registrations.models import Role, CustomUser
from User_Registrations.models import Group
from . import roles
# from User_Registration.groups import Group
gamer_role = Role.objects.create(name="Gamer")

gamer_role_user, created = CustomUser.objects.get_or_create(username='gamer_username')
if created:
    gamer_role_user.set_password('password123') 
    gamer_role_user.save()

gamer_group, _ = Group.objects.get_or_create(name='Gamer')
gamer_role_user.groups.add(gamer_group)

# permissions_to_add_to_gamer = [
#     Permission.objects.get(codename='view_customuser'),
#     Permission.objects.get(codename='create_customuser'),
#     Permission.objects.get(codename='update_customuser'),
#     Permission.objects.get(codename='select_scenario'),
#     Permission.objects.get(codename='view_gamer_profile'),
#     Permission.objects.get(codename='change_gamer_profile'),
# ]

# gamer_role.permissions.add(*permissions_to_add_to_gamer)
from django.contrib.auth.models import Permission

# Define a list of codenames for the permissions you want
permission_codenames = [
    'view_customuser',
    'create_customuser',
    'update_customuser',
    'select_scenario',
    'view_gamer_profile',
    'change_gamer_profile',
]

# Retrieve the permissions that match the codenames using the filter() method
permissions_to_add_to_gamer = Permission.objects.filter(codename__in=permission_codenames)

# Add the retrieved permissions to the gamer_role
gamer_role.permissions.add(*permissions_to_add_to_gamer)


admin_role = Role.objects.create(name="Administrator")

# create the admin user
admin_user, created = CustomUser.objects.get_or_create(username='admin_username')
if created:
    admin_user.set_password('adminpass')  
    admin_user.save()

administrator_group, _ = Group.objects.get_or_create(name='Administrator')
admin_user.groups.add(administrator_group)

permissions_to_add_to_admin = [
    Permission.objects.get(codename='add_customuser'),
    Permission.objects.get(codename='change_customuser'),
    Permission.objects.get(codename='delete_customuser'),
    Permission.objects.get(codename='delete_scenario'),
    Permission.objects.get(codename='edit_scenario'),
    Permission.objects.get(codename='edit_rewards'),
    Permission.objects.get(codename='delete_rewards'),
    Permission.objects.get(codename='edit_Scenario List'),
    Permission.objects.get(codename='delete_Scenario List'),
    Permission.objects.get(codename='add_role'),
    Permission.objects.get(codename='change_role'),
    Permission.objects.get(codename='delete_role'),
    Permission.objects.get(codename='view_permission'),
    Permission.objects.get(codename='add_permission'),
    Permission.objects.get(codename='change_permission'),
    Permission.objects.get(codename='delete_permission'),
    Permission.objects.get(codename='manage_settings'),
    Permission.objects.get(codename='view_logs'),
    Permission.objects.get(codename='perform_maintenance'),
    Permission.objects.get(codename='view_reports'),
    Permission.objects.get(codename='view_gamer_profile'),
    Permission.objects.get(codename='view_administrator_dashboard'),
]

admin_role.permissions.add(*permissions_to_add_to_admin)

user1 = CustomUser.objects.create_user(username='gamer1', password='password123', phone_number='+254')
user1.roles.add(gamer_role)

user2 = CustomUser.objects.create_user(username='admin1', password='adminpass', phone_number='254')
user2.roles.add(admin_role)
print(user1)