from django.urls import path
from .views import ProductListCreate, ProductAPIView


urlpatterns = [
    path("", ProductListCreate.as_view()),
    path("detail/<int:pk>/", ProductAPIView.as_view())
]