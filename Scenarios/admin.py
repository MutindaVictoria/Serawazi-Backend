from django.contrib import admin
from .models import Levels, Scenarios

class LevelsAdmin(admin.ModelAdmin):
    list_display = ['level_title']

class ScenariosAdmin(admin.ModelAdmin):
    list_display = ['background_info', 'correct_answer', 'incorrect_answer', 'image', 'level']

admin.site.register(Levels, LevelsAdmin)
admin.site.register(Scenarios, ScenariosAdmin)
