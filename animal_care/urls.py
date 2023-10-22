from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import AnimalCareListView, AnimalCareCreateView

urlpatterns = [
    path('',AnimalCareListView.as_view()),
    path('create/',AnimalCareCreateView.as_view())
]
