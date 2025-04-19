from django import forms
from pets.models import Appointment

# class PersonForm(forms.ModelForm):
    
#     class Meta:
#         model = Person
#         fields = ["first_name", "", "", "", ]

# class AddressForm(forms.ModelForm):
    
#     class Meta:
#         model = Address
#         fields = ['street', 'uni_number', 'city','province','postal_code','country']

# class AppointmentForm(forms.ModelForm):

#     class Meta:
#         model = Appointment
#         # Not having duration as a filed as it is defaulted to 1 hour and should be only changed by admin
#         fields = ["reason"]
#         # widgets = {
#         #     'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         # }
        

