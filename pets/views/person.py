from typing import Any
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from pets.models.person import Person
from pets.models.appointment import Appointment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pets.forms import PersonForm

from django.utils import timezone


# Person CRUD


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm 

    #PV: Delete this - get the form and use queryset to filter the appointment 
    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        # Only show future appointment objects + appointment not booked by other person using related name
        form.fields["appointment"].queryset = Appointment.objects.filter(appointment_date__gt=timezone.now()).filter(people_at_this_appointment__isnull=True)
        form.fields["appointment"].empty_label = "Select an appointment"
        return form

    # def get_context_data(self, **kwargs) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         context['appointment_form'] = AppointmentForm(self.request.POST)
    #     else:
    #          # empty form
    #          context['appointment_form'] = AppointmentForm()
    #     return context
    
    # def form_valid(self, form):

    #     context = self.get_context_data()
    #     appointment_form = context['appointment_form']

    #     if appointment_form.is_valid():
    #         person = form.save(commit=False)
    #         selected_appointment = form.cleaned_data['appointment']
    #         # Update appointment reason
    #         #selected_appointment.reason = appointment_form.cleaned_data['reason']
    #         selected_appointment.save()

    #         person.save()
    #         return redirect(person.get_absolute_url())
    #     else:
    #         return self.form_invalid(form)



class PersonListView(ListView):
    model = Person
    pag = 20

class PersonDetailView(DetailView):
    model = Person

class PersonUpdateView(UpdateView):
    model = Person
    fields = [
        "first_name",
        "last_name",
        "phone",
        "email",
        "interested_species",
        "first_time_owner"
    ]


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy("people_list")



    
