from rest_framework import serializers
from mytrip import models

class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.City
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Trip
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Photo
        fields = '__all__'