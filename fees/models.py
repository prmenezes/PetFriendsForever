from django.db import models

# Create your models here.

class PetFee(models.Model):

    pet_type_choices = {
        "dog": "Dog",
        "cat": "Cat",
        "bird": "Bird"
    }

    type = models.CharField(choices=pet_type_choices, max_length=50)
    # TODO: Rename this field to 'category'
    # TODO: Add category to pets model. When the pet is being given up for adoption, depending on the category, the staff can see the fees for that pet.
    age_category = models.CharField(max_length=100)
    fees = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.type} ({self.age_category}): {self.fees}"