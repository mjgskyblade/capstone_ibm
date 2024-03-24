# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    # Define the fields for the Car Make model

    # - Name
    name = models.CharField(max_length=100)

    # - Description
    description = models.TextField()

    # - Any other fields you would like to include in car make model

    # - __str__ method to print a car make object
    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
class CarModel(models.Model):
    # - Name
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    # - Type (CharField with a choices argument to provide limited choices
    # such as Sedan, SUV, WAGON, etc.)
    TYPE_CHOICES = (
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    # - Year (IntegerField) with min value 2015 and max value 2023
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])

    # - Any other fields you would like to include in car model

    # - __str__ method to print a car make object
    def __str__(self):
        return f"{self.make.name} - {self.name}"
