from django.http import HttpResponse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from pets.models.pets import Pet
from pets.models.person import Person

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from typing import Any


# Create your views here.


class HomeView(View):
    def get(self, request):
        context = {"NA": "NA"}
        return render(request, "home.html", context)


# PV - see if it can be changed to TemplateView
class FilteredPetView(ListView):
    model = Pet
    template_name = "filtered_pets.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        pet_type = self.kwargs.get("pet_type")
        if pet_type:
            context["filtered_pets_list"] = Pet.objects.filter(type__iexact=pet_type)
            context["pet_type"] = pet_type
        else:
            context["filtered_pets_list"] = Pet.objects.all()
        return context


class PetListView(ListView):
    model = Pet


class PetDetailView(DetailView):
    model = Pet


# Person CRUD


class PersonCreateView(CreateView):
    model = Person
    fields = [
        "first_name",
        "last_name",
        "phone",
        "email",
        "interested_species",
        "first_time_owner"
    ]

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


class ContactFormSuccessView(TemplateView):
    template_name = "contact_form_success.html"

    
