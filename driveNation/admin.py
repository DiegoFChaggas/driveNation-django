from django.contrib import admin

from .models import NaturalPerson, Vehicle, Rental, Maintenance, Payment,License, VehicleGroup, Address
class NaturalPersonAdmin(admin.ModelAdmin):
    ...
admin.site.register(NaturalPerson, NaturalPersonAdmin)
class VehicleAdmin(admin.ModelAdmin):
    ...
admin.site.register(Vehicle, VehicleAdmin)
class RentalAdmin(admin.ModelAdmin):
    ...
admin.site.register(Rental, RentalAdmin)
class MaintenanceAdmin(admin.ModelAdmin):
    ...
admin.site.register(Maintenance, MaintenanceAdmin)
class PaymentAdmin(admin.ModelAdmin):
    ...
admin.site.register(Payment, PaymentAdmin)

class LicenseAdmin(admin.ModelAdmin):
    ...
admin.site.register(License, LicenseAdmin)

class VehicleGroupAdmin(admin.ModelAdmin):
    ...
admin.site.register(VehicleGroup, VehicleGroupAdmin)

class AddressAdmin(admin.ModelAdmin):
    ...
admin.site.register(Address, AddressAdmin)
