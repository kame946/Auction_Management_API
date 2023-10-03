from django.urls import path
from .views import UserRegistrationView, UserDetailsView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('<int:pk>/', UserDetailsView.as_view(), name='user-details'),
]
