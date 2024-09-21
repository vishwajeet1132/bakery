from rest_framework import generics
from .models import BakeryItem
from .serializers import BakeryItemSerializer

class BakeryItemCreateView(generics.CreateAPIView):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

class BakeryItemDetailView(generics.RetrieveAPIView):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

class BakeryItemListView(generics.ListAPIView):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer