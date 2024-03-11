from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import AnimalCareListView, AnimalCareCreateView, AnimalCareEditView, MakeOfferView, CancelOffer, AcceptOffer

urlpatterns = [
    path('',AnimalCareListView.as_view()),
    path('create/',AnimalCareCreateView.as_view()),
    path('<int:pk>/',AnimalCareEditView.as_view()),
    path('<int:pk>/make-offer/',MakeOfferView.as_view(), name="make-offer", ),
    path('offer/<int:pk>/cancel/',CancelOffer.as_view(), name="cancel-offer", ),
    path('offer/<int:pk>/accept/',AcceptOffer.as_view(), name="accept-offer", ),
]
