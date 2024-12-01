from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    zip_code = models.CharField(max_length=9, verbose_name="CEP")  # Ex.: 12345-678
    street = models.CharField(max_length=255, verbose_name="Endereço")
    number = models.CharField(max_length=10, verbose_name="Número")
    complement = models.CharField(max_length=255, blank=True, null=True, verbose_name="Complemento")
    neighborhood = models.CharField(max_length=100, verbose_name="Bairro")
    country = models.CharField(max_length=100, verbose_name="País")
    state = models.CharField(max_length=100, verbose_name="Estado")
    city = models.CharField(max_length=100, verbose_name="Cidade")

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return f"{self.endereco}, {self.numero} - {self.cidade}/{self.estado}"

class NaturalPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="natural_person")
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Endereço")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class VehicleGroup(models.Model):
    abbreviation = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    default_daily_price = models.DecimalField(max_digits=8, decimal_places=2)
    default_weekly_price = models.DecimalField(max_digits=8, decimal_places=2)
    default_monthly_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.abbreviation} - {self.name}"
    
    
class Vehicle(models.Model):
    group = models.ForeignKey(VehicleGroup, on_delete=models.CASCADE, related_name="vehicles")
    plate = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year_of_manufacture = models.IntegerField()
    color = models.CharField(max_length=20)
    chassis = models.CharField(max_length=20, unique=True)
    renavam = models.CharField(max_length=11, unique=True)
    fuel_type = models.CharField(max_length=20, choices=[
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ])
    image = models.ImageField(upload_to='vehicles/images/%Y/%m/%d/')
    title = models.TextField()
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title


    
class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rent_start_date = models.DateField()
    rent_end_date = models.DateField()
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Rental of {self.vehicle.plate} by {self.user.email}'
    
# Table: Maintenance
class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Maintenance for {self.vehicle.plate}' 


# Table: Payment
class Payment(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f'Payment for Rental {self.rental.id}'

# Table: Rental (Aluguel)

class License(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=11, unique=True)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    category = models.CharField(max_length=10)
    issuing_agency = models.CharField(max_length=255)

    def __str__(self):
        return self.license_number


