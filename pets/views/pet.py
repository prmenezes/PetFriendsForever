from django.views.generic import ListView, DetailView

from pets.models.pets import Pet
from typing import Any




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

