"""
URL configuration for pff project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from pets.views.home import HomeView
from pets.views.pet import FilteredPetView, PetListView, PetDetailView
from pets.views.contact_form_success import ContactFormSuccessView

from pets.views.views import (
    PersonCreateView,
    PersonListView,
    PersonDetailView,
    PersonUpdateView,
    PersonDeleteView
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("pets/", PetListView.as_view(), name="pet_list"),
    path("pets/<int:pk>/", PetDetailView.as_view(), name="pet_details"),
    path("pets/<str:pet_type>/", FilteredPetView.as_view(), name="filtered_pet_list"),
    path("people/", PersonCreateView.as_view(), name="list_people"),
    path("people/<int:pk>/", PersonDetailView.as_view(), name="person_details"),
    path("people/create/", PersonCreateView.as_view(), name="create_person"),
    path("people/edit/", PersonUpdateView.as_view(), name="update_person"),
    path("people/delete/<int:pk>", PersonDeleteView.as_view(), name="delete_person"),
    path("people/create/success", ContactFormSuccessView.as_view(), name="contact_form_success"),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
