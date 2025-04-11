from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from pets.models.person import Person
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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



    
