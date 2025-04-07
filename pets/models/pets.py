from django.db import models

import uuid

class Pet(models.Model):
    
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    adoption_status = models.CharField(max_length=100)
    adopted_by = models.ForeignKey("Person", on_delete=models.SET_NULL, related_name="pets", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
