from django.shortcuts import render 
from .models import Flight
from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):

    try:
        flight = Flight.objects.get(pk=flight_id)
        print(flight)

    except Flight.DoesNotExist:
        return HttpResponseNotFound("<h1 style='text-align:center; margin-top:300px'>404 - This flight does not exist!</h1>")

    return render(request, "flights/flight.html", {
        "flight": flight,
        # "passengers" is that related name i described in Models
        "passengers":flight.passengers.all()
    })

