from django.db import models
from scenario_collection.models import ScenarioCollection

class Scenarios(models.Model):
    RIGHT_CHOICE = 'Right'
    WRONG_CHOICE = 'Wrong'
    DECISION_CHOICES = [
        (RIGHT_CHOICE, 'Right'),
        (WRONG_CHOICE, 'Wrong'),
    ]

    scenario_level = models.IntegerField()
    scenario_title = models.CharField(max_length=255, unique=True)  # Ensure scenario_title is unique
    Background_info = models.TextField(max_length=255)
    Decision_options = models.CharField(max_length=255, choices=DECISION_CHOICES)
    Reward_points = models.IntegerField()
    
    scenario_collection = models.ForeignKey(ScenarioCollection, on_delete=models.CASCADE)

    def __str__(self):
        return self.scenario_title

class Answer(models.Model):
    scenario = models.ForeignKey(Scenarios, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text
