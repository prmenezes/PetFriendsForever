from django.views.generic import TemplateView

class ContactFormSuccessView(TemplateView):
    template_name = "contact_form_success.html"