# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer
from datetime import date
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin


class AddItemView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def post(self, request):
        try:
            name = request.data.get('name')
            quantity = float(request.data.get('quantity'))
            expiry = request.data.get('expiry')
            unit = request.data.get('unit')
            price_per_unit = float(request.data.get('price_per_unit'))

            # Check if an item with the same name and expiry already exists
            inventory_item = Inventory.objects.filter(name=name, expiry=expiry, unit=unit).first()

            if inventory_item:
                # Add quantity to existing item
                inventory_item.quantity += quantity
                inventory_item.save()
            else:
                # Create a new inventory item if expiry differs
                new_item_data = {
                    "name": name,
                    "quantity": quantity,
                    "expiry": expiry,
                    "unit": unit,
                    "price_per_unit": price_per_unit
                }
                serializer = InventorySerializer(data=new_item_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Item added successfully."}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RemoveItemView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def post(self, request):
        try:
            name = request.data.get('name')
            quantity_to_remove = float(request.data.get('quantity'))

            # Fetch non-expired items of the same name, ordered by nearest expiry
            items = Inventory.objects.filter(name=name, expiry__gte=date.today()).order_by('expiry')

            if not items:
                return Response({"message": "No valid items to remove."}, status=status.HTTP_400_BAD_REQUEST)

            total_removed = 0

            for item in items:
                if item.quantity >= quantity_to_remove:
                    # If the current item has enough quantity, deduct and break
                    item.quantity -= quantity_to_remove
                    item.save()
                    total_removed += quantity_to_remove
                    break
                else:
                    # If current item doesn't have enough, consume all and move to the next
                    quantity_to_remove -= item.quantity
                    total_removed += item.quantity
                    item.quantity = 0
                    item.save()

            return Response({"message": f"{total_removed} units of {name} removed."}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ListItemsView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]

    def get(self, request):
        try:
            items = Inventory.objects.all().order_by('name', 'expiry')
            serializer = InventorySerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ListExpiredItemsView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request):
        try:
            expired_items = Inventory.objects.filter(expiry__lt=date.today()).order_by('expiry')
            serializer = InventorySerializer(expired_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



