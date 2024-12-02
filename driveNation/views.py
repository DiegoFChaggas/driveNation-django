from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

from django.contrib import messages
import re

from .models import Vehicle, NaturalPerson, Address, License
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


def register(request):
    if request.method == 'POST':
        # Extraindo dados do formulário
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('senha')
        cpf = data.get('cpf')
        name = data.get('nomeUsuario')
        birth_date = data.get('dtNasc')
        sex = data.get('sexo')

        # Endereço
        zip_code = data.get('cep')
        street = data.get('endereco')
        number = data.get('numero')
        complement = data.get('complemento')
        neighborhood = data.get('bairro')
        country = data.get('pais')
        state = data.get('estado')
        city = data.get('cidade')

        # Habilitação
        license_number = data.get('numeroHabilitacao')
        issue_date = data.get('dtEmissao')
        expiration_date = data.get('dtValidade')
        category = data.get('categoria')
        issuing_agency = data.get('orgaoEmissor')

        user = User.objects.filter(username=username).first()
        
        if user:
            return messages.error(request, "Usuário já existe.")
        
        user = User.objects.create_user(username=username, email=email, password=password)
            
        address = Address.objects.create(
                    zip_code=zip_code,
                    street=street,
                    number=number,
                    complement=complement,
                    neighborhood=neighborhood,
                    country=country,
                    state=state,
                    city=city
                )

                # Criar NaturalPerson
        natural_person = NaturalPerson.objects.create(
                    user=user,
                    cpf=cpf,
                    name=name,
                    birth_date=birth_date,
                    sex=sex,
                    address=address
                )

                # Criar licença
        License.objects.create(
                    user=user,
                    license_number=license_number,
                    issue_date=issue_date,
                    expiration_date=expiration_date,
                    category=category,
                    issuing_agency=issuing_agency
                )

        messages.success(request, "Usuário cadastrado com sucesso!")
        
        return redirect('login')
        
    return render(request, "driveNation/register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect('home')
        
        else:
            return redirect('login')
    return render(request, "driveNation/login.html")


@login_required(login_url="/login")
def vehicle(request):
    vehicles = Vehicle.objects.all()
    return render(request, "driveNation/vehicle.html", context={
        'vehicles': vehicles,
    })
    
@login_required(login_url="/login")
def rental(request,id):
    vehicles = get_object_or_404(Vehicle, id=id)
        
    return render(request, "driveNation/rental.html", context={
        'vehicles': vehicles,
    })


