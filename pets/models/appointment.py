from django.utils.timezone import localtime 
from django.db import models
from datetime import timedelta

from user_profile.models import UserProfile

# TODO: Re-think the whole appointment system. Or at the least, have a calendar widget to select from instead of a drop down.

class Appointment(models.Model):

    appointment_reason_choices = {
        "pet_visit": "Meet and greet pet(s)",
        "general": "Meet staff member/General queries",
        "pet_pickup": "Picking up an approved pet",
        "other": "Other"
    }

    appointment_date = models.DateTimeField(blank=True, null=True)
    appointment_duration = models.DurationField(default=timedelta(hours=1))
    reason = models.CharField(default="other", blank=True, null=True, choices=appointment_reason_choices)
    is_booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, related_name='appointments')


    def __str__(self):
        # Return appointment date and time in 21-Apr-2025 11AM format
        if self.appointment_date:
            local_dt = localtime(self.appointment_date)
            return f"{local_dt.strftime('%d-%b-%Y %I%p')} - {'Booked' if self.is_booked else 'Available'}"
        return "Appointment (unscheduled)"


             



    
     


