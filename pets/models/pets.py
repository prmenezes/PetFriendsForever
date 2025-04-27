from django.db import models
from user_profile.models import UserProfile

from django.urls import reverse

import uuid

class Pet(models.Model):

    pet_type_choices = {
        "Dogs": "Dog",
        "Cats": "Cat",
        "Birds": "Bird"
    }

    adoption_status_choices = {
        "adoptable": "Adoptable",
        "in_progress": "In Progress",
        "approved": "Approved",
        "adopted": "Adopted"
    }

    gender_choices = {
        "female": "female",
        "male": "male"
    }


    
    # TODO: Auto generate random ids that are unique
    id = models.IntegerField(primary_key=True)
    type = models.CharField(choices=pet_type_choices)
    name = models.CharField(max_length=100)
    # TODO: Use birthday - Date field to store the birthday and a method that returns the age as of today
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=gender_choices)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=1200)
    adoption_status = models.CharField(choices=adoption_status_choices)
    adopted_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name="pets", blank=True, null=True)
    display_pic = models.ImageField(
        upload_to="pet_display_pics_upload",
        default="pet_pics_upload/photo_coming_soon.png", 
        max_length=200
    )

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("pet_details", kwargs={"pk": self.pk})
    