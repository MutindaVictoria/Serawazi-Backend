from django.db import models

# Create your models here.

class Badges(models.Model):
    name = models.CharField(unique=True,max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='badge_images/')

    def __str__(self):
        return self.name  
    
    
class ScenarioCollection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cover_Image = models.ImageField(upload_to='covers/')
    total_Scenarios = models.IntegerField(default=0)

    def calculate_total_scenarios(self):
        total = ScenarioCollection.objects.filter(name=self.name).count()
        return total

    def save(self, *args, **kwargs):
        self.total_Scenarios = self.calculate_total_scenarios()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Category(models.Model):
    Category_Options = models.CharField(max_length=255, choices=[('Finance Bill', 'Finance Bill'), ('Bill of Rights', 'Bill of Rights')])
    Daily_Updates = models.TextField()
    Category_Image = models.ImageField(upload_to='images/')
    Is_Active = models.BooleanField()

    def __str__(self):
        return self.Category_Options  
    


class VirtualItem(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
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
    
    scenario_collection = models.ForeignKey(ScenarioCollection, on_delete=models.CASCADE, related_name='api_scenarios')

    def __str__(self):
        return self.scenario_title

class Answer(models.Model):
    scenario = models.ForeignKey(Scenarios, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text
