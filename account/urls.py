from django.urls import path, include
from .views import UserDetailView, UserRegisterView

urlpatterns = [
    path('details/', UserDetailView.as_view()),
    path('register/', UserRegisterView.as_view()),
]