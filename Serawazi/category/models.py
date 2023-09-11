from django.db import models

class Category(models.Model):
    Category_Options = models.CharField(max_length=255, choices=[('option1', 'Option 1'), ('option2', 'Option 2')])
    Daily_Updates = models.TextField()
    Category_Image = models.ImageField(upload_to='category_images/')
    Is_Active = models.BooleanField()

    def __str__(self):
        return self.Category_Options  


