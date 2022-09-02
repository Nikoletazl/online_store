from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=100000,
        decimal_places=2
    )

    def __str__(self):
        return self.title


class Order(models.Model):
    date = models.DateField(
        auto_now_add=True,
    )
    products = models.ManyToManyField(
        Product,
        blank=True,
        related_name='orders'
    )


