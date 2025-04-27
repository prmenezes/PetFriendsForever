from django.contrib import admin

from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display=["user", "first_name", "last_name", "email", "interested_species", "first_time_owner" ]

    #Since id is FK
    # def get_id_type(self, obj):
    #     return obj.id_proof.id_type if obj.id_proof else "—"
    
    # get_id_type.short_description = "ID Type"


admin.site.register(UserProfile, UserProfileAdmin)