from django.shortcuts import render

cars = [
    {   
        'title'    : 'GRUPO CE - ECONÔMICO C/AR',
        'subtitle' : 'Hyundai HB20S 1.0, GM Onix 1.0, VW Voyage 1.0 ou similar*',
        'price' : 79.95,
        'img'   : '../static/images/onix.png'
    },
    {   
        'title'    : 'GRUPO P -  4X4 ESPECIAL ',
        'subtitle' : 'GM S10 2.8 Turbo, Mitsubishi L200 2.5, Toyota Hilux 2.8 Turbo ou similar*',
        'price' : 345.95,
        'img'   : '../static/images/vehicles/4x4.png'
    },
    {   
        'title'    : 'GRUPO L - EXECUTIVO',
        'subtitle' : 'Toyota Corolla 2.0, GM Cruze 1.4 Turbo ou similar*',
        'price' : 241.95,
        'img'   : '../static/images/vehicles/executives.png'
    }
]

def home(request):
    return render(request, "driveNation/index.html")

def vehicle(request):
    informations = {
        'cars' : cars, 
    }
    return render(request, "driveNation/vehicle.html", informations)
