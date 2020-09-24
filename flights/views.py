from django.shortcuts import render 
from .models import Flight
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):

    try:
        flight = Flight.objects.get(pk=flight_id)

    except flight_id.DoesNotExist:
        raise Http404('<h1>Page not found</h1>')
    
    return render(request, "flights/flight.html", {
        "flight": flight,
        # "passengers" is that related name i described in Models
        "passengers":flight.passengers.all()
    })