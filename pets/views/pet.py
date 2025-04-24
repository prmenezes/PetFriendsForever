from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib import messages

from pets.models.pets import Pet
from typing import Any



class PetListView(ListView):
    # Lists all pets or filters them according to type
    model = Pet
    

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

class PetCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Pet
    #template_name = "pet_form.html"
    fields = [
        "id",
        "type",
        "name",
        "age",
        "gender",
        "breed",
        "description",
        "adoption_status",
        "adopted_by",
        "display_pic"

    ]

    def test_func(self):

        return self.request.user.is_staff


class PetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pet
    
    fields = [
         "type",
        "name",
        "age",
        "gender",
        "breed",
        "description",
        "adoption_status",
        "adopted_by",
        "display_pic"
    ]

    template_name_suffix = "_update_form"

    #PV: staff user can see pet detail even if status changes to adopted, so get_abs_url is ok
    #success_url = reverse_lazy("pet_list")

    def test_func(self):

        return self.request.user.is_staff
    

class PetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pet
    template_name_suffix = "_confirm_delete"
    #When a pet is deleted, it'll redirect you to address list
    success_url = reverse_lazy("pet_list")

    def post(self, request, *args, **kwargs):
        messages.success(request, "Pet deleted successfully.")
        return super().post(request, *args, **kwargs)
    
    # Post calls delete, but for some reason the re-direction is happening so fast that the message does not appear
    # def delete(self, request, *args, **kwargs):
    #     messages.success(request, "Pet deleted successfully.")
    #     return super().delete(request, *args, **kwargs)

    def test_func(self):

        return self.request.user.is_staff

class UnadoptablePetListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    # Lists all pets or filters them according to type
    model = Pet
    template_name = "unadoptable_pets.html"
    

    def get_queryset(self):
        queryset = super().get_queryset()

        #Future scope: If we want to display all pets - adoptable + inProgress + pending + adopted - i.e. url - pets/all
        #if pet_type == 'all', return queryset

        # Filter queryset by all available pets 
        queryset = Pet.objects.exclude(adoption_status__iexact ='adoptable')

        #Get the pet_type if filtered by type and change the queryset to further filter only available 'pet_types'
        # pet_type = self.kwargs.get("pet_type")
        # if pet_type:
        #     queryset = queryset.filter(type__iexact=pet_type)
        
        return queryset
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # If filtered by 'pet_type' list, add the pet type to context
        # pet_type = self.kwargs.get("pet_type")
        # if pet_type:
        #     context["pet_type"] = pet_type
     
        return context
    
    def test_func(self):

        return self.request.user.is_staff