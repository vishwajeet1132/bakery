from django.urls import path
from .views import AddItemView, RemoveItemView, ListItemsView, ListExpiredItemsView

urlpatterns = [
    path('add-item/', AddItemView.as_view(), name='add-item'),
    path('remove-item/', RemoveItemView.as_view(), name='remove-item'),
    path('list-items/', ListItemsView.as_view(), name='list-items'),
    path('list-expired-items/', ListExpiredItemsView.as_view(), name='list-expired-items'),
]
