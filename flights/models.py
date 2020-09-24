from django.db import models

# Create your db models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    #related_name is for accessing this data in reverse e.g get all departures and arrivals given a code or city
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # This is to return formated string when querying db
    def __str__(self):
        return f"{self.origin} to {self.destination}, duration {self.duration}min"
