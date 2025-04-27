import uuid
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class UserProfile(models.Model):

    species_choices = {
        "DOG": "dog",
        "CAT": "cat",
        "BIRD": "bird"
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # PV: Phone number = whole number
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    interested_species = models.CharField(choices=species_choices, blank=True, null=True)
    first_time_owner = models.BooleanField(help_text="Please check this box if this will be your first pet")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user})"
    
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})

