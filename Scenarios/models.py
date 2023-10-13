from django.db import models

class Levels(models.Model):
    LEVEL_CHOICES = (
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3'),  
        (4, 'Level 4'),         
    )
    level_title = models.CharField(max_length=256)  
    
    def __str__(self):
        return self.level_title 

class Scenarios(models.Model):
    background_info = models.TextField(default='')
    correct_answer = models.TextField(max_length=255)
    incorrect_answer = models.TextField(max_length=255)
    image = models.URLField(max_length=2000)
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.background_info

