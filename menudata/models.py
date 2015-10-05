from django.db import models
from datetime import date

class Resturant(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)

class MenuItems(models.Model):
    date = models.DateField(default=date.today, blank=True, null=True)
    food = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    resturant = models.ForeignKey(Resturant)

