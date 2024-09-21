from django.db import models


class Inventory(models.Model):
    UNIT_CHOICES = [
        ('KG', 'Kilogram'),
        ('LTR', 'Litre')
    ]

    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    expiry = models.DateField()
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.get_unit_display()}"

    class Meta:
        verbose_name_plural = "Inventory"
