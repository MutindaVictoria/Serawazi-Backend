from django.db import models

class Category(models.Model):
    Category_Options = models.CharField(max_length=255, choices=[('Finance Bill', 'Finance Bill'), ('Bill of Rights', 'Bill of Rights')])
    Daily_Updates = models.TextField()
    Category_Image = models.ImageField(upload_to='images/')
    Is_Active = models.BooleanField()

    def __str__(self):
        return self.Category_Options  


