from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    car = 'car'
    truck = 'truck'
    van = 'van'
    suv = 'SUV'
    vehicle_type_choices = [(car, 'Car'), (truck, 'Truck'), (van, 'Van'), (suv, 'SUV')]
    vehicle_type = models.CharField(max_length = 6, choices = vehicle_type_choices, default = car)
    seats = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=5, decimal_places=2)
    reserved = models.BooleanField(default = False)
    rented = models.BooleanField(default = False)
    available = models.BooleanField(default = True)
    reserved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='vehicle_pics')

    if rented == True:
        available = False

    def __str__(self):
        return str(self.seats) + ' Seat ' + self.vehicle_type.title()