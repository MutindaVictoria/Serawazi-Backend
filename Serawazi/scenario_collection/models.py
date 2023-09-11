from django.db import models

class ScenarioCollection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cover_Image = models.ImageField(upload_to='covers/')  
    total_Scenarios = models.PositiveIntegerField()

    def __str__(self):
        return self.name
