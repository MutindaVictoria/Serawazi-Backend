from django.contrib import admin
from .models import ScenarioCollection 

@admin.register(ScenarioCollection)
class ScenarioCollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cover_Image', 'total_Scenarios')
