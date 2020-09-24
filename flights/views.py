from django.shortcuts import render 
from .models import Flight, Passenger
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):

    try:
        flight = Flight.objects.get(pk=flight_id)

    except Flight.DoesNotExist:
        return HttpResponseNotFound("<h1 style='text-align:center; margin-top:300px'>404 - This flight does not exist!</h1>")

    return render(request, "flights/flight.html", {
        "flight": flight,
        # "passengers" is that related name i described in Models
        "passengers": flight.passengers.all(),
        # Exclude all passengers whose this flight is already in flights of theirs
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))

