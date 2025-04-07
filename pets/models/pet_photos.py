from django.db import models


class PetPhotos(models.Model):
    images = models.ImageField(
        upload_to="pet_pics_upload",
        height_field="image_height",
        width_field="image_width",
        null=True,
        blank=True,
    )
    alternate_text = models.CharField(blank=True, max_length=50)
    display_pic = models.BooleanField(blank=True, null=True)
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE, related_name="pet_photos")

    def __str__(self):
        return f"{self.pet.name}'s pic"