from rest_framework import serializers
from mytrip import models

class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.City
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    source_city = CitySerializer(read_only=True)
    source_city_id = serializers.PrimaryKeyRelatedField(queryset=models.City.objects.all(), write_only=True, source='source_city')
    destination_city = CitySerializer(read_only=True)
    destination_city_id = serializers.PrimaryKeyRelatedField(queryset=models.City.objects.all(), write_only=True, source='destination_city')
    class Meta:
        model = models.Trip
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Photo
        fields = '__all__'