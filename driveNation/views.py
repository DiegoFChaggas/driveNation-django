from django.shortcuts import render
from .models import Vehicle, VehiclePrice

cars = [
    {   
        'title'    : 'GRUPO CE - ECONÔMICO C/AR',
        'subtitle' : 'Hyundai HB20S 1.0, GM Onix 1.0, VW Voyage 1.0 ou similar*',
        'price' : 79.95,
        'img'   : '../../static/images/onix.png',
        'link'  : 'economic'
    },
    {   
        'title'    : 'GRUPO P -  4X4 ESPECIAL ',
        'subtitle' : 'GM S10 2.8 Turbo, Mitsubishi L200 2.5, Toyota Hilux 2.8 Turbo ou similar*',
        'price' : 345.95,
        'img'   : '../../static/images/vehicles/4x4.png',
        'link'  : '4x4'
    },
    {   
        'title'    : 'GRUPO L - EXECUTIVO',
        'subtitle' : 'Toyota Corolla 2.0, GM Cruze 1.4 Turbo ou similar*',
        'price' : 241.95,
        'img'   : '../../static/images/vehicles/executives.png',
        'link'  : 'executive'
    }
]

car = [
    {
        
    }
]

def home(request):
    informations = {
        'cars' : cars, 
    }
    return render(request, "driveNation/index.html", informations)

def vehicle(request):
    vehicles = Vehicle.objects.all()
    price = VehiclePrice.objects.all()
    return render(request, "driveNation/vehicle.html", context={
        'vehicles': vehicles,
        'prices' : price,
    })

def register(request):
    return render (request, "driveNation/register.html")

def login(request):
    return render(request, "driveNation/login.html")

def location(request,id):
    return render(request, "driveNation/location.html")