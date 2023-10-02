from django.contrib import admin
from .models import Scenarios  # Use a relative import here

# Register your models here.
class ScenariosAdmin(admin.ModelAdmin):

    list_display = ('scenario_level', 'scenario_title', 'Background_info', 'correct_answer','incorrect_answer','image',)

admin.site.register(Scenarios, ScenariosAdmin)


