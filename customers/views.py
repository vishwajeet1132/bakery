from rest_framework import generics
from Kitchen.models import BakeryItem
from .serializers import BakeryItemSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer,PastOrderSerializer
from rest_framework.pagination import PageNumberPagination

class BakeryItemListView(generics.ListAPIView):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination



class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated (JWT)

class PastOrdersView(generics.ListAPIView):
    serializer_class = PastOrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination # Ensure the user is authenticated (JWT)

    def get_queryset(self):
        # Return only the orders of the authenticated user
        return Order.objects.filter(customer=self.request.user)
