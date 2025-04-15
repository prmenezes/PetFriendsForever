from django.db import models

import uuid

class Pet(models.Model):

    pet_type_choices = {
        "Dogs": "Dog",
        "Cats": "Cat",
        "Birds": "Bird"
    }
    
    id = models.IntegerField(primary_key=True)
    type = models.CharField(choices=pet_type_choices)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=1200)
    adoption_status = models.CharField(max_length=100)
    adopted_by = models.ForeignKey("Person", on_delete=models.SET_NULL, related_name="pets", blank=True, null=True)
    display_pic = models.ImageField(
        upload_to="pet_display_pics_upload",
        default="pet_pics_upload/photo_coming_soon.png", 
        max_length=200
    )

    def __str__(self):
        return f"{self.name}"
