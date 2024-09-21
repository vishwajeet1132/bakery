from django.urls import path
from .views import BakeryItemListView,CreateOrderView, PastOrdersView

urlpatterns = [
    path('items/', BakeryItemListView.as_view(), name='list-items'),
    path('create-order/', CreateOrderView.as_view(), name='create-order'),
    path('orders/', PastOrdersView.as_view(), name='orders'),

]