from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import AnimalListCreate, AnimalRetrieve


urlpatterns = [
       path('', AnimalListCreate.as_view()),
       path('<id>', AnimalRetrieve.as_view()),
]
