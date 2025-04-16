from django.db import models

# Create your models here.

class PetAdoptionFeesMixin(models.Model):

    category = models.CharField(primary_key=True, max_length=50)
    adoption_fees = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"Pet: {self.category}: {self.adoption_fees}"

class DogAdoptionFees(PetAdoptionFeesMixin, models.Model):

    def __str__(self):
        return f"Dog: {self.category}: {self.adoption_fees}"
    
class CatAdoptionFees(PetAdoptionFeesMixin, models.Model):

    def __str__(self):
        return f"Cat: {self.category}: {self.adoption_fees}"
    
class BirdAdoptionFees(PetAdoptionFeesMixin, models.Model):

    def __str__(self):
        return f"Bird: {self.category}: {self.adoption_fees}"
