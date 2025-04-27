from django.urls import path
from .views import UserProfileCreateView, UserProfileUpdateView, UserProfileDeleteView, UserProfileDetailView
from .views import AvailableAppointmentListView, BookAppointmentView, UserAppointmentListView, AppointmentUpdateView, CancelAppointmentView 

urlpatterns = [
    path('profile/create/', UserProfileCreateView.as_view(), name='profile_create'),
    path('profile/update/<uuid:pk>/', UserProfileUpdateView.as_view(), name='profile_update'),
    path('profile/delete/<uuid:pk>/', UserProfileDeleteView.as_view(), name='profile_delete'),
    path('profile/<uuid:pk>/', UserProfileDetailView.as_view(), name='profile_detail'),

    path('available_appointments/', AvailableAppointmentListView.as_view(), name='available_appointments'),
    path('my_appointments/', UserAppointmentListView.as_view(), name='user_appointments'),
    path('available_appointments/book/<int:pk>/', BookAppointmentView.as_view(), name='book_appointment'),
    path('available_appointments/edit/<int:pk>/', AppointmentUpdateView.as_view(), name='edit_appointment'),
    path('available_appointments/cancel/<int:pk>/', CancelAppointmentView.as_view(), name='cancel_appointment'),

]