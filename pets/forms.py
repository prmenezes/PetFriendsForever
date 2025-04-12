from django import forms


class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        exclude = []

# class AddressForm(forms.ModelForm):
    
#     class Meta:
#         model = Address
#         fields = ['street', 'uni_number', 'city','province','postal_code','country']

