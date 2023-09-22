from django.contrib import admin

# Register your models here.
from .models import Badges

class Bagdes_admin(admin.ModelAdmin):
    list_display = ("name", "description", "image")

admin.site.register(Badges,Bagdes_admin)