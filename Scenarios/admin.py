from django.contrib import admin
from .models import Scenarios  # Use a relative import here

# Register your models here.
class ScenariosAdmin(admin.ModelAdmin):

    list_display = ('scenario_level', 'scenario_title', 'Background_info', 'Reward_points', 'correct_answer','incorrect_answer',)

admin.site.register(Scenarios, ScenariosAdmin)


