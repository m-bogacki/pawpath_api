from .serializers import AnimalCareListSerializer, AnimalCareCreateSerializer, OfferSerializer
from .models import AnimalCare, Offer

from rest_framework import generics, views, response
from rest_framework import status
from rest_framework import generics, views, response, status
from rest_framework import generics, views, response, status
from .serializers import OfferSerializer
from .models import Offer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class AnimalCareListView(generics.ListAPIView):
    queryset = AnimalCare.objects.all()
    serializer_class = AnimalCareListSerializer
    permission_classes = [AllowAny]



@extend_schema(request=AnimalCareCreateSerializer, responses=AnimalCareListSerializer)
class AnimalCareCreateView(generics.CreateAPIView):
    queryset = AnimalCare.objects.all()
    serializer_class = AnimalCareCreateSerializer
    permission_classes = [IsAuthenticated]


    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_animal_care_animals = serializer.validated_data.get('animals')
        existing_animal_care = AnimalCare.objects.filter(animals__in=new_animal_care_animals, status__in=["New", "Ongoing"]).first()
        
        if existing_animal_care:
            raise ValueError("Animal Care already exists for selected animal.")
        self.perform_create(serializer)

        response_serializer = AnimalCareListSerializer(instance=serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return response.Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


                
class AnimalCareEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalCare.objects.all()
    serializer_class = AnimalCareListSerializer
    permission_classes = [IsAuthenticated]


    
    

class MakeOfferView(views.APIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

    
    def post(self, request, pk):
        animal_care = AnimalCare.objects.get(pk=pk)
        user_offer = animal_care.offers.filter(carrer=request.user)
        if user_offer:
            return response.Response({"message": "You have already made an offer for this animal care."}, status=status.HTTP_400_BAD_REQUEST)
        
        description = request.data.get('description')
        offer = Offer.objects.create(carrer=request.user, animal_care=animal_care, status="Proposed", description=description)
        serializer = OfferSerializer(offer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class CancelOffer(views.APIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer 
    authentication_classes = [IsAuthenticated]
    
    def get(self, _, offer_id):
        try:
            offer = Offer.objects.get(pk=offer_id)
            offer.status = "Declined"
            offer.save()
            return response.Response(status=status.HTTP_200_OK)
        except Offer.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)



class AcceptOffer(views.APIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

        
    def get(self, _, pk):
        try:
            offer = Offer.objects.get(pk=pk)
            offer.status = "Accepted"
            offer.animal_care.status = "Ongoing"
            offer.animal_care.save()
            offer.save()
            return response.Response(status=status.HTTP_200_OK)
        except Offer.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
