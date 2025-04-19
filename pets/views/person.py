from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from pets.models.person import Person
from pets.models.appointment import Appointment
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils import timezone


# Person CRUD


class PersonCreateView(CreateView):
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

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        # Only show future appointment objects + appointment not booked by other person using related name
        form.fields["appointment"].queryset = Appointment.objects.filter(appointment_date__gt=timezone.now()).filter(people_at_this_appointment__isnull=True)
        return form

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



    
