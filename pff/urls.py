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
from django.urls import path, include

from pets.views.home import HomeView
from pets.views.pet import PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView, UnadoptablePetListView
from pets.views.contact_form_success import ContactFormSuccessView
from pets.views.how_to_adopt import HowtoAdoptView
from pets.views.search_pets import SearchPetView

from fees.views import FeesView

from contact_us.views import ContactUsView

from pets.views.person import (
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
    path("pets/unadoptable_pets", UnadoptablePetListView.as_view(), name="unadoptable_pet_list"),

    path("pets/<int:pk>/", PetDetailView.as_view(), name="pet_details"),
    path("pets/filter/<str:pet_type>/", PetListView.as_view(), name="filtered_pet_list"),

    
    path("pets/create/", PetCreateView.as_view(), name="create_pet"),
    path("pets/edit/<int:pk>/", PetUpdateView.as_view(), name="edit_pet"),
    path("pets/delete/<int:pk>/", PetDeleteView.as_view(), name="delete_pet"),



    path("people/", PersonDetailView.as_view(), name="list_people"),
    path("people/<int:pk>/", PersonDetailView.as_view(), name="person_details"),
    path("people/create/", PersonCreateView.as_view(), name="create_person"),
    path("people/edit/<int:pk>/", PersonUpdateView.as_view(), name="update_person"),
    path("people/delete/<int:pk>", PersonDeleteView.as_view(), name="delete_person"),
    path("people/create/success/", ContactFormSuccessView.as_view(), name="contact_form_success"),

    path("contact_us/", ContactUsView.as_view(), name="contact_us"),

    path("search/<str:name>/", SearchPetView.as_view(), name="search"),
    path("how_to_adopt/", FeesView.as_view(), name="how_to_adopt"),


    path('users/', include("users.urls")),
    path('user_profile/', include("user_profile.urls"))

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
