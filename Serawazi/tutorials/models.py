from django.db import models

class Tutorial(models.Model):
    introduction_texts = models.TextField(unique=True)
    image = models.ImageField(upload_to='badge_images/')
    description_texts=models.TextField(max_length=255)
    gamified_elements = models.CharField(max_length=255, choices=[('option1', 'Option 1'), ('option2', 'Option 2')])

    def __str__(self):
        return self.description_texts