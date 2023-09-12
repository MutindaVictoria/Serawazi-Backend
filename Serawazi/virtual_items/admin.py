from django.contrib import admin
from .models import VirtualItem


class VirtualItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
admin.site.register(VirtualItem, VirtualItemAdmin)