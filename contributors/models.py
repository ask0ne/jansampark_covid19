from django.db import models

# Create your models here.
PRODUCTS = (
        ("Select", "Select"),
        ("Masks", "Masks"),
        ("Ventilators", "Ventilators"),
        ("Medicines & medical equipments", "Medicines & medical equipments"),
        ("Rooms", "Rooms"),
        ("Beds", "Beds"),
        ("Food", "Food"),
)


class Retailer(models.Model):
    """Retailers enter the availability of their products"""
    company_name = models.CharField(max_length=255)
    product = models.CharField(max_length=80, choices=PRODUCTS, default='Select')
    quantity = models.IntegerField(default=0)
    coordinates = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}_{}".format(self.company_name, self.product, self.quantity)


