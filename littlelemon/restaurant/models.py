from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )  # Entre 1 et 100 invités
    bookingDate = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.no_of_guests} guests on {self.bookingDate.strftime('%d/%m/%Y')}"

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.title} : {self.price}"