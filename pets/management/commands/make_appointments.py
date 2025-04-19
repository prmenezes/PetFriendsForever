from django.core.management.base import BaseCommand
from datetime import datetime, timedelta, time
from pets.models import Appointment  

class Command(BaseCommand):
    help = 'Generate appointment slots for the next 7 days from 11am to 4pm (1-hour slots)'

    def handle(self, *args, **kwargs):
        start_hour = 11
        end_hour = 16 
        num_days = 7

        now = datetime.now()
        today = now.date()

        appointments_created = []

        # for tomorrow to next 7 days
        for day in range(1, num_days + 1):
            appointment_date = today + timedelta(days=day)

            # from 11am to 3pm
            for hour in range(start_hour, end_hour):
                # date + time
                dt = datetime.combine(appointment_date, time(hour, 0))

                # if appointment not already created, create
                appointment, created = Appointment.objects.get_or_create(appointment_date=dt)
                if created:
                    appointments_created.append(appointment)

        print(f"Created {len(appointments_created)} appointment times.")