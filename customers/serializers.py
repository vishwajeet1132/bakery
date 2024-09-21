from rest_framework import serializers
from .models import Order, OrderItem
from Kitchen.models import BakeryItem

class BakeryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryItem
        fields = ['name', 'selling_price','id']




class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['bakery_item', 'cost']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    product_ids = serializers.ListField(write_only=True, child=serializers.IntegerField())

    class Meta:
        model = Order
        fields = ['id', 'items', 'total_cost', 'product_ids']  # No customer field here!

    def create(self, validated_data):
        # The customer is taken from the request context (authenticated user)
        customer = self.context['request'].user  # This uses JWT token for authentication
        product_ids = validated_data.pop('product_ids', [])
        total_cost = 0

        # Create the order for the authenticated customer
        order = Order.objects.create(customer=customer)

        for product_id in product_ids:
            try:
                # Fetch the product from BakeryItem
                bakery_item = BakeryItem.objects.get(id=product_id)
                item_cost = bakery_item.selling_price

                # Create an OrderItem
                OrderItem.objects.create(
                    order=order,
                    bakery_item=bakery_item.name,
                    cost=item_cost
                )

                total_cost += item_cost

                # Remove the bakery item from the bakery after selling
                bakery_item.delete()

            except BakeryItem.DoesNotExist:
                raise serializers.ValidationError(f"Bakery item with id {product_id} not found.")

        # Update the total cost of the order
        order.total_cost = total_cost
        order.save()

        return order



class PastOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['total_cost', 'created_at']