from django.db import models

# Create your models here.
class Scenarios (models.Model):
    scenario_level = models.IntegerField()
    scenario_title = models.CharField(max_length=255)
    Background_info = models.TextField(max_length=255)
    Decision_options = models.CharField(max_length=255)
    Reward_points = models.IntegerField()

    def __str__(self):
        return self.scenario_title
