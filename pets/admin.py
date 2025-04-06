from django.contrib import admin

from pets.models import Pet

# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display=["name", "type"]


admin.site.register(Pet, PetAdmin)



