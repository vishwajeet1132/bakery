from rest_framework import serializers
from .models import BakeryItem, BakeryItemIngredient

class BakeryItemIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryItemIngredient
        fields = ['id','name', 'quantity_percentage', 'cost_price']

class BakeryItemSerializer(serializers.ModelSerializer):
    ingredients = BakeryItemIngredientSerializer(many=True)

    class Meta:
        model = BakeryItem
        fields = ['id','name', 'cost_price', 'selling_price', 'ingredients']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        bakery_item = BakeryItem.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            BakeryItemIngredient.objects.create(bakery_item=bakery_item, **ingredient_data)
        return bakery_item
