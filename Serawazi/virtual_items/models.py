from django.db import models

class VirtualItem(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='virtual_items/')

    def __str__(self):
        return self.name
