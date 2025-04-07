from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from pets.models.pets import Pet


# Create your views here.
class PetView(ListView):

    model = Pet


class PetDetailView(DetailView):

    model = Pet
