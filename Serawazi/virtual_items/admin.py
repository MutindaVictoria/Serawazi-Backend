from django.contrib import admin
from .models import VirtualItem

@admin.register(VirtualItem)
class VirtualItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
