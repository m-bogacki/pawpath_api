from django.urls import path
from .views import AnimalList, AnimalCreate, AnimalRetrieveUpdateDestroyView, CareInstructionsUpdate


urlpatterns = [
       path('', AnimalList.as_view()),
       path('<int:pk>/update-care-instructions/', CareInstructionsUpdate.as_view()),
       path('<int:pk>/', AnimalRetrieveUpdateDestroyView.as_view()),
       path('create/', AnimalCreate.as_view()),
]
