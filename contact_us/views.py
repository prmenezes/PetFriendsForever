# Create your views here.
from django.views.generic import TemplateView

from .models import ContactInfo, HoursOfOperation


class ContactUsView(TemplateView):

    template_name = "contact_us.html"

    def get_context_data(self, **kwargs) -> dict[str, str]:
        context = super().get_context_data(**kwargs)
        
        context["contact"] = ContactInfo.objects.first()
        context["hours_of_operation"] = HoursOfOperation.objects.all()
        return context
    