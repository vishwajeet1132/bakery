from django.db import models
from Inventory.models import Inventory


class Kitchen(models.Model):
    product_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Inventory, through='KitchenItem')

    def __str__(self):
        return self.product_name


class KitchenItem(models.Model):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity_used = models.FloatField()  # How much of this inventory item is used

    def save(self, *args, **kwargs):
        # Reduce quantity in the inventory when an item is used in the kitchen
        if self.quantity_used <= self.inventory_item.quantity:
            self.inventory_item.quantity -= self.quantity_used
            self.inventory_item.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Insufficient inventory for the requested quantity.")

    def __str__(self):
        return f"{self.quantity_used} {self.inventory_item.get_unit_display()} of {self.inventory_item.name} for {self.kitchen.product_name}"

