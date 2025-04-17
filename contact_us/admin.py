from django.contrib import admin

# Register your models here.
from .models import ContactInfo, HoursOfOperation
# Register your models here.
class ContactInfoAdmin(admin.ModelAdmin):

    list_display = ["phone", "email", "address"]

class HoursOfOperationAdmin(admin.ModelAdmin):

    list_display = ["day", "start_time", "end_time"]

admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(HoursOfOperation, HoursOfOperationAdmin)

