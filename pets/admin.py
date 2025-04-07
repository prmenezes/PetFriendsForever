from django.contrib import admin

from pets.models import Pet, Person, Address, Appointment, IDProof, PetPhotos

# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display=["id", "name", "type", "adoption_status", "adopted_by"]


class PersonAdmin(admin.ModelAdmin):
    list_display=["first_name", "last_name", "email", "appointment", "get_id_type" ]

    def get_id_type(self, obj):
        return obj.id_proof.id_type if obj.id_proof else "—"
    get_id_type.short_description = "ID Type"

class AddressAdmin(admin.ModelAdmin):
    pass

class AppointmentAdmin(admin.ModelAdmin):
    pass

class IDProofAdmin(admin.ModelAdmin):
    pass

class PetPhotosAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pet, PetAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(IDProof, IDProofAdmin)
admin.site.register(PetPhotos, PetPhotosAdmin)





