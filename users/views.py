from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class RegisterView(FormView):

    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account created!')
        return super().form_valid(form)
    
# No need for login and logout views as they are in built in Django authentication views


