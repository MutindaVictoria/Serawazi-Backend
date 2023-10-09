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
    

class Levels(models.Model):
    LEVEL_CHOICES = (
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3'),  
        (4, 'Level 4'),         
    )
    level_title = models.CharField(max_length=255)  
    
    def __str__(self):
        return self.get_level_title_display()  

class Scenarios(models.Model):
    background_info = models.TextField()
    correct_answer = models.TextField(max_length=255)
    incorrect_answer = models.TextField(max_length=255)
    image = models.ImageField(upload_to='covers/')
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.background_info