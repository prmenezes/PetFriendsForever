from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import PetFee

# Create your views here.
class FeesView(ListView):

    model = PetFee
    template_name = "how_to_adopt.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["dog_fees"] = PetFee.objects.filter(type__iexact='dog')
        context["cat_fees"] = PetFee.objects.filter(type__iexact='cat')
        context["bird_fees"] = PetFee.objects.filter(type__iexact='bird')

        return context
    