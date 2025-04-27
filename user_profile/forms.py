from django import forms
from user_profile.models import UserProfile
from pets.models import Appointment

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "phone", "email", "interested_species", "first_time_owner"]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["interested_species"].required = False


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment    
        fields = ["reason"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reason'].label = "Reason for Appointment"

