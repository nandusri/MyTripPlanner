from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CitySerializer, TripSerializer, PhotoSerializer
from .models import City, Trip, Photo

# Create your views here.
class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    
    def get_queryset(self):
        queryset = Trip.objects.filter(user = self.request.user.id)
        return queryset

class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()