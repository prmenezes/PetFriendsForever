from django.urls import path
from .views import UserProfileCreateView, UserProfileUpdateView, UserProfileDeleteView, UserProfileDetailView

urlpatterns = [
    path('profile/create/', UserProfileCreateView.as_view(), name='profile_create'),
    path('profile/update/<uuid:pk>/', UserProfileUpdateView.as_view(), name='profile_update'),
    path('profile/delete/<uuid:pk>/', UserProfileDeleteView.as_view(), name='profile_delete'),
    path('profile/<uuid:pk>/', UserProfileDetailView.as_view(), name='profile_detail'),
]