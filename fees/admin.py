from django.contrib import admin
from .models import PetFee
# Register your models here.
class PetFeeAdmin(admin.ModelAdmin):

    list_display = ["type", "age_category", "fees"]


admin.site.register(PetFee, PetFeeAdmin)