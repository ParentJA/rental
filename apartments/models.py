__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Third-party imports...
from localflavor.us.models import PhoneNumberField, USStateField, USZipCodeField

# Django imports...
from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = USStateField()
    zip_code = USZipCodeField()
    manager = models.CharField(max_length=250)
    phone_number = PhoneNumberField()

    def __unicode__(self):
        return self.address


class Apartment(models.Model):
    building = models.ForeignKey('apartments.Building', related_name='apartments')
    amenities = models.ManyToManyField('apartments.Amenity', related_name='apartments')
    apartment_type = models.CharField(max_length=250)
    apartment_number = models.CharField(max_length=3)
    num_bathrooms = models.FloatField()
    num_bedrooms = models.IntegerField()
    num_rooms = models.IntegerField()
    rate = models.IntegerField()

    def __unicode__(self):
        return '%s, Unit %s' % (self.building.address, self.apartment_number)


class Amenity(models.Model):
    description = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Amenities'

    def __unicode__(self):
        return self.description


class Guest(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField()

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Booking(models.Model):
    apartment = models.ForeignKey('apartments.Apartment', related_name='bookings')
    guest = models.ForeignKey('apartments.Guest', related_name='bookings')
    status = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return '%s: %s' % (self.apartment, self.status)
