# from django.contrib import admin
# from .models import User_Registration

# # Register your models here.
# class User_RegistrationAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'password', 'username')  

# admin.site.register(User_Registration, User_RegistrationAdmin)


# from django.contrib import admin
# from User_Registration.models import Admin, RegularUser

# class AdminsAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name')
#     search_fields = ('first_name', 'last_name', 'email')
#     list_filter = ('usrname',)

# class RegularUserAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email')
#     search_fields = ('first_name', 'last_name', 'email')

# admin.site.register(Admin, AdminAdmin)
# admin.site.register(RegularUser, RegularUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Admins, Gamer




class AdminsAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'password')
admin.site.register(Admins,AdminsAdmin)

class GamerAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')
admin.site.register(Gamer,GamerAdmin)