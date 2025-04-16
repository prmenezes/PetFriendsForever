from django.contrib import admin

# Register your models here.

# from pets.models import Pet, Person, Address, Appointment, IDProof, PetPhotos

# # Register your models here.

# class PetAdmin(admin.ModelAdmin):
#     list_display=["id", "name", "type", "adoption_status", "adopted_by"]


from adoption_fees.models import DogAdoptionFees, CatAdoptionFees, BirdAdoptionFees

class DogAdoptionFeesAdmin(admin.ModelAdmin):
    list_display=["category", "adoption_fees"]

class CatAdoptionFeesAdmin(admin.ModelAdmin):
    list_display=["category", "adoption_fees"]

class BirdAdoptionFeesAdmin(admin.ModelAdmin):
    list_display=["category", "adoption_fees"]

admin.site.register(DogAdoptionFees, DogAdoptionFeesAdmin)
admin.site.register(CatAdoptionFees, CatAdoptionFeesAdmin)
admin.site.register(BirdAdoptionFees, BirdAdoptionFeesAdmin)
