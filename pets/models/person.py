from django.db import models

import uuid

from django.urls import reverse

class Person(models.Model):

    species_choices = {
        "DOG": "dog",
        "CAT": "cat",
        "BIRD": "bird"
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # PV: Phone number = whole number
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    interested_species = models.CharField(choices=species_choices, blank=True, null=True)
    first_time_owner = models.BooleanField(help_text="Please check this box if this will be your first pet")
    appointment = models.OneToOneField("Appointment", 
                                    on_delete=models.SET_NULL, 
                                    related_name="people_at_this_appointment",
                                    blank=True, 
                                    null=True
                                    )

    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse("contact_form_success")

