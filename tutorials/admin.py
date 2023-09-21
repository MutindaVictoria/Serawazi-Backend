from django.contrib import admin
from .models import Tutorial  

# Register your models here.
from .models import Tutorial

class Tutorial_admin(admin.ModelAdmin):
    list_display = ("introduction_texts", "image", "description_texts", "gamified_elements")
    
admin.site.register(Tutorial,Tutorial_admin)  

    