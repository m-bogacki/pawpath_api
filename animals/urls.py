from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import AnimalList, AnimalCreate, AnimalRetrieve


urlpatterns = [
       path('', AnimalList.as_view()),
       path('create/', AnimalCreate.as_view()),
       path('<id>', AnimalRetrieve.as_view()),
]
