from django.views.generic import ListView, DetailView

from pets.models.pets import Pet
from typing import Any



class PetListView(ListView):
    model = Pet
    

# Need an exclude filter for any pet that has been adopted
    def get_queryset(self):
        queryset = super().get_queryset()

        #Future scope: If we want to display all pets - adoptable + inProgress + pending + adopted - i.e. url - pets/all
        #if pet_type == 'all', return queryset

        # Filter queryset by all available pets 
        queryset = Pet.objects.filter(adoption_status__iexact='adoptable')

        #Get the pet_type if filtered by type and change the queryset to further filter only available 'pet_types'
        pet_type = self.kwargs.get("pet_type")
        if pet_type:
            queryset = queryset.filter(type__iexact=pet_type)
        
        return queryset
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # If filtered by 'pet_type' list, add the pet type to context
        pet_type = self.kwargs.get("pet_type")
        if pet_type:
            context["pet_type"] = pet_type
     
        return context


class PetDetailView(DetailView):
    model = Pet

