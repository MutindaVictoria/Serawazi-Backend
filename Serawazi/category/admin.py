from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category_Options', 'Is_Active',)
    list_filter = ('Is_Active',)
    search_fields = ('Category_Options', 'Daily_Updates',)
admin.site.register(Category, CategoryAdmin)