from django.contrib import admin
from .models import ScenarioCollection

class ScenarioCollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cover_Image', 'total_Scenarios')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    readonly_fields = ('total_Scenarios',)

admin.site.register(ScenarioCollection, ScenarioCollectionAdmin)
