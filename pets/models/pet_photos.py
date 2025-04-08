from django.db import models


class PetPhotos(models.Model):
    image = models.ImageField(
        upload_to="pet_pics_upload",
        height_field="image_height",
        width_field="image_width",
    )
    alternate_text = models.CharField(blank=True, max_length=50)
    display_pic = models.BooleanField(blank=True, null=True)
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE, related_name="pet_photos")

    image_width = models.PositiveIntegerField(null=True, blank=True)  # Stores the width in pixels
    image_height = models.PositiveIntegerField(null=True, blank=True) # Stores the height in pixels

    def __str__(self):
        return f"{self.pet.name}'s pic"