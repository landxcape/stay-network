from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.db import models


class User(AbstractUser):
    pass


class Rental(models.Model):
    renter = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="rents"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    location = models.CharField(max_length=255)
    geo_location = models.PointField(geography=True, null=True)
    no_of_rooms = models.PositiveIntegerField()
    rent_type = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    facilities = models.TextField(max_length=255)
    parking = models.BooleanField(default=False)
    availability = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "renter": self.renter.username,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "geo_location": self.geo_location,
            "no_of_rooms": self.no_of_rooms,
            "rent_type": self.rent_type,
            "floor": self.floor,
            "facilities": self.facilities,
            "parking": self.parking,
            "availability": self.availability,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
        }
