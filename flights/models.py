from django.db import models

# Create your db models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    # This is to return formated string when querying db
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}, duration {self.duration}min"

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"