from django.db import models
from model_utils.models import TimeStampedModel
import users.models

class City(TimeStampedModel):
    city_name = models.CharField(max_length = 300)
    # location = models.MultiPointField()

    def __str__(self):
        return self.city_name

class Trip(TimeStampedModel):
    user = models.ForeignKey(users.models.User, on_delete=models.CASCADE)
    city = models.ManyToManyField(City)

    def __str__(self):
        return self.user.username

class Photo(TimeStampedModel):
    city_photo = models.ImageField(upload_to='trip')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.trip)