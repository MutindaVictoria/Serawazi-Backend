from django.contrib import admin
from .models import ScenarioCollection  # Import your model here

@admin.register(ScenarioCollection)
class ScenarioCollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cover_Image', 'total_Scenarios')
