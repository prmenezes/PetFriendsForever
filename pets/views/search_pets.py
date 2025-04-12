from django.views.generic import ListView, DetailView

from pets.models.pets import Pet
from typing import Any




# PV - see if it can be changed to TemplateView
class SearchPetView(ListView):
    model = Pet
    template_name = "search.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        # Search only adoptable pets
        queryset = queryset.filter(adoption_status__iexact="adoptable")

        # Get the search name
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(name__iexact=search_query)
        
        return queryset

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["pet_name"] = self.request.GET.get('q').capitalize()
        return context
    

    



class PetListView(ListView):
    model = Pet


