from django.db import models


class PetPhotos(models.Model):
    image = models.ImageField(
        upload_to="pet_pics_upload",
        default="pet_pics_upload/photo_coming_soon.png",
        blank=True,
        null=True
    )
    alternate_text = models.CharField(blank=True, max_length=50)
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE, related_name="pet_photos")

    def __str__(self):
        return f"{self.pet.name}'s pic"