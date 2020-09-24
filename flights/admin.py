from django.contrib import admin
from .models import  Airport, Flight, Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display = ["id", "origin", "destination", "duration"]

class AirportAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "city"]

class PassengerAdmin(admin.ModelAdmin):
    list_display = ["id", "first", "last"]

# Register your models here.
admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)