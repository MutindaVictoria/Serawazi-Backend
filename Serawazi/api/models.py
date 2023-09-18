from django.db import models

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



