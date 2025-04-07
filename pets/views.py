from django.http import HttpResponse

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from pets.models.pets import Pet


# Create your views here.

class PetView(View):

    def get(self, request, pet_type):

        pet_filter = Pet.objects.filter(type__iexact=pet_type)

        context = {
            "filtered_pets":pet_filter
        }

        return render(request, "filtered_pets.html", context)


class PetListView(ListView):

    model = Pet


class PetDetailView(DetailView):

    model = Pet


