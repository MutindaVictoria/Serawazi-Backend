from django.contrib import admin
from .models import Category

<<<<<<< HEAD
@admin.register(Category)
=======

>>>>>>> 94138d22fc74e82a1495a31cee23f19c2fbd1054
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category_Options', 'Is_Active',)
    list_filter = ('Is_Active',)
    search_fields = ('Category_Options', 'Daily_Updates',)
<<<<<<< HEAD
=======
admin.site.register(Category, CategoryAdmin)
>>>>>>> 94138d22fc74e82a1495a31cee23f19c2fbd1054
