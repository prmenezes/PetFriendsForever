from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from user_profile.models import UserProfile
from user_profile.forms import UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from pets.models import Appointment
from .forms import AppointmentForm

from django.utils import timezone
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect


# Create your views here.

# User Profile Views

class UserProfileCreateView(LoginRequiredMixin, CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "user_profile/userprofile_form.html"

    def form_valid(self, form):

        # Check if a profile already exists for this user
        if UserProfile.objects.filter(user=self.request.user).exists():

            existing_profile = UserProfile.objects.get(user=self.request.user)
            # Redirect to a page (or you can show a message if you prefer)
            messages.info(self.request, "You already have a profile. Redirecting to your profile.")

            return redirect('profile_detail', pk=existing_profile.pk)  # or wherever you want to redirect
        
        # If profile does not exist for this user
        # Get user profile 
        user_profile = form.instance

        # Link this profile to logged in user
        user_profile.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ["first_name", "last_name", "phone", "email", "interested_species", "first_time_owner"]

    template_name = "user_profile/userprofile_update_form.html"

    def get_queryset(self):
        return UserProfile.objects.filter(user = self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})        

class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = "user_profile/userprofile_confirm_delete.html"

    def get_queryset(self):
        return UserProfile.objects.filter(user = self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('home')

class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = "user_profile/userprofile_detail.html"


# Appointment Views

# Mixin to make sure appointment views can only be accessed if user has created a profile. 
# Since the appointment model has a booked by profile field
class ProfileRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'user_profile'):
            return redirect('profile_create')  # Redirect to the profile creation page
        return super().dispatch(request, *args, **kwargs)

class AvailableAppointmentListView(LoginRequiredMixin, ProfileRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/available_appointments_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        queryset =  super().get_queryset().filter(appointment_date__gte=timezone.now(), is_booked=False).order_by('appointment_date')
        return queryset

    # def get_queryset(self):
    #     return Appointment.objects.all()

class BookAppointmentView(LoginRequiredMixin, ProfileRequiredMixin, FormView):

    form_class = AppointmentForm
    template_name = 'appointments/book_appointment.html'

    def dispatch(self, request, *args, **kwargs):

        # Call the ProfileRequiredMixin's dispatch explicitly to check if the user has a profile 
        # so that two dispatches don't cause a conflict
        response = ProfileRequiredMixin.dispatch(self, request, *args, **kwargs)
        if response:
            return response
        
        self.appointment = get_object_or_404(Appointment, pk=kwargs['pk'], is_booked=False)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        appointment = self.appointment
        appointment.reason = form.cleaned_data['reason']
        appointment.is_booked = True
        appointment.booked_by = self.request.user.user_profile
        appointment.save()

        return redirect('user_appointments')
    
class UserAppointmentListView(LoginRequiredMixin, ProfileRequiredMixin, ListView):
    template_name = 'appointments/user_appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(booked_by=self.request.user.user_profile).order_by('appointment_date')
    
class AppointmentUpdateView(LoginRequiredMixin, ProfileRequiredMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/book_appointment.html'

    def get_queryset(self):
        return Appointment.objects.filter(booked_by=self.request.user.user_profile)

    def get_success_url(self):
        return reverse_lazy('user_appointments')
    

class CancelAppointmentView(LoginRequiredMixin, ProfileRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Get the appointment by ID and make sure it is not already booked
        appointment = get_object_or_404(Appointment, pk=kwargs['pk'], booked_by=request.user.user_profile)

        # Cancel the appointment by setting the necessary fields
        appointment.is_booked = False
        appointment.booked_by = None
        appointment.reason = "other"
        appointment.save()

        # Redirect to the list of user appointments after cancellation
        return redirect('user_appointments')
    


