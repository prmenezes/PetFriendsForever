from django.db import models

# Create your models here.
class ContactInfo(models.Model):

    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"office_contact_info:{self.email}"
    
class HoursOfOperation(models.Model):
    _DAYS_OF_THE_WEEK = {
        'Mon': 'Monday',
        'Tue': 'Tuesday',
        'Wed': 'Wednesday',
        'Thu': 'Thursday',
        'Fri': 'Friday',
        'Sat': 'Saturday',
        'Sun': 'Sunday'
    }

    day = models.CharField(choices=_DAYS_OF_THE_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day}: {self.start_time} to {self.end_time}"
    
    def get_day_name(self):
        """Returns the day in full eg. Monday instead of Mon
        """
        
        return self._DAYS_OF_THE_WEEK[self.day]
    