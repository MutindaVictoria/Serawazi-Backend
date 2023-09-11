from django.contrib import admin
from .models import User_Registration

# Register your models here.
class User_RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'password', 'username')  

admin.site.register(User_Registration, User_RegistrationAdmin)
