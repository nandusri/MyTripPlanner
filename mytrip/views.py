from django.shortcuts import render
from .serializers import CitySerializer, TripSerializer, PhotoSerializer
from .models import City, Trip, Photo

# Create your views here.
class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()

class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]
    queryset = Trip.objects.all()

class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()