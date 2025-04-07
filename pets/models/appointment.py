from django.db import models
from datetime import timedelta

class Appointment(models.Model):

    appointment_reason_choices = {
        "pet_visit": "Meet and greet pet(s)",
        "general": "Meet staff member/General queries",
        "pet_pickup": "Picking up an approved pet",
        "other": "Other"
    }

    appointment_date = models.DateTimeField(blank=True, null=True)
    appointment_duration = models.DurationField(default=(timedelta(hours=1)))
    reason = models.CharField(blank=True, null=True, choices=appointment_reason_choices)


    def __str__(self):
        return f"Appointment time - {self.appointment_date}"

