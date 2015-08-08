__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Third-party imports...
from rest_framework import views
from rest_framework.response import Response

# Local imports...
from .models import Amenity, Apartment, Building
from .serializers import AmenitySerializer, ApartmentSerializer, BuildingSerializer


class ApartmentAPIView(views.APIView):
    def get(self, request, pk=None):
        data = {
            'building': BuildingSerializer(Building.objects.all(), many=True).data,
            'apartment': ApartmentSerializer(Apartment.objects.all(), many=True).data,
            'amenity': AmenitySerializer(Amenity.objects.all(), many=True).data
        }

        return Response(data)
