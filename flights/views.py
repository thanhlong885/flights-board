from django.shortcuts import render
from .models import Flight
# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/flights.html", context)

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    context = {
        "flight": flight,
        "passengers": flight.passengers.all()
    }
    return render(request, "flights/flight-detail.html", context)

