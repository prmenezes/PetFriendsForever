from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.
class PetView(View):

    def get(self,request):
        return HttpResponse("A list of animals")