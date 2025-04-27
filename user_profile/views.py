from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from user_profile.models import UserProfile
from user_profile.forms import UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.

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


class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = "user_profile/userprofile_confirm_delete.html"

    def get_queryset(self):
        return UserProfile.objects.filter(user = self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('home')

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "user_profile/userprofile_detail.html"
