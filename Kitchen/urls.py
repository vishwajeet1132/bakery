
from django.urls import path
from .views import BakeryItemCreateView, BakeryItemDetailView,BakeryItemListView

urlpatterns = [
    path('create/', BakeryItemCreateView.as_view(), name='bakery-item-create'),
    path('items/', BakeryItemListView.as_view(), name='bakeryitem-list'),
    path('items/<int:pk>/', BakeryItemDetailView.as_view(), name='bakery-item-detail')
]