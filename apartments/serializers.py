__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Standard library imports...
from rest_framework import serializers

# Local imports...
from .models import Amenity, Apartment, Building


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('id', 'description')


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = (
            'id', 'building', 'amenities', 'apartment_type', 'apartment_number', 'num_bathrooms', 'num_bedrooms',
            'num_rooms', 'rate'
        )


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = (
            'id', 'name', 'description', 'address', 'city', 'state', 'zip_code', 'manager', 'phone_number'
        )
