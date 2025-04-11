from django.views.generic import TemplateView

import calendar

class ContactUsView(TemplateView):

    template_name = "contact_us.html"
    
    _HOURS = {
        "weekday": "10am - 7pm",
        "weekends": "9am - 4pm"
}
    

    def get_context_data(self, **kwargs) -> dict[str, str]:
        context = super().get_context_data(**kwargs)
        
        #Get days of the week
        weekdays = list(calendar.day_name[0:5])
        weekends = list(calendar.day_name[5:7])

        hours_of_operation = {}
        for day in weekdays + weekends:
            if day in weekdays:
                hours_of_operation[day] = self._HOURS.get("weekday")
            else:
                hours_of_operation[day] = self._HOURS["weekends"]
        

        context["hours_of_operation"] = hours_of_operation
        return context
    