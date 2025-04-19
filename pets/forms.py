from django import forms
from django.utils import timezone

from pets.models import Appointment, Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "interested_species",
            "first_time_owner",
            "appointment"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter available appointments
        self.fields["appointment"].queryset = Appointment.objects.filter(
            appointment_date__gt=timezone.now(),
            people_at_this_appointment__isnull=True
        )
        self.fields["appointment"].empty_label = "Select an appointment"

    def clean_appointment(self):
        appointment = self.cleaned_data.get("appointment")
        if not appointment:
            raise forms.ValidationError("Please select an appointment.")
        return appointment

