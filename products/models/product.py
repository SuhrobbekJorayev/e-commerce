from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def is_in_stock(self):
        return self.stock > 0

    def decrease_stock(self, quantity):
        if quantity > self.stock:
            return False

        self.stock -= quantity
        self.save()
        return True

    def increase_stock(self, quantity):
        self.stock += quantity
        self.save()

    class Meta:
        ordering = ['name']
