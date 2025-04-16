from django.db import models

# Create your models here.

class PetFee(models.Model):

    pet_type_choices = {
        "dog": "Dog",
        "cat": "Cat",
        "bird": "Bird"
    }

    type = models.CharField(choices=pet_type_choices, max_length=50)
    age_category = models.CharField(max_length=100)
    fees = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.type} ({self.age_category}): {self.fees}"