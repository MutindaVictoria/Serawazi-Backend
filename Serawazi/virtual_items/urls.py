from django.urls import path
from .views import VirtualItemListCreateView, VirtualItemDetailView

urlpatterns = [
    path('virtual-items/', VirtualItemListCreateView.as_view(), name='virtual-item-list-create'),
    path('virtual-items/<int:pk>/', VirtualItemDetailView.as_view(), name='virtual-item-detail'),
]
