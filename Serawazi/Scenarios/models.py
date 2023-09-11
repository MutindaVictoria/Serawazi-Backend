from django.db import models

# Create your models here.
class Scenarios (models.Model):
    scenario_level = models.IntegerField()
    scenario_title = models.CharField()
    Background_info = models.TextField()
    Decision_options = models.CharField()
    Reward_points = models.IntegerField()
