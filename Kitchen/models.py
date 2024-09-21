from django.db import models


class BakeryItem(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class BakeryItemIngredient(models.Model):
    bakery_item = models.ForeignKey(BakeryItem, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity_percentage = models.FloatField()  # Percentage of this ingredient in the bakery item
    cost_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)

    def __str__(self):
        return f"{self.name} in {self.bakery_item.name}"
