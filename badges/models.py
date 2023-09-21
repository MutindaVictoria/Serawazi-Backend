from django.db import models

class Badges(models.Model):
    name = models.CharField(unique=True,max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='badge_images/')

    def __str__(self):
        return self.name  