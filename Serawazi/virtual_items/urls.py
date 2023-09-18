from django.urls import path
from .views import  VirtualItemDetail, VirtualItemUpdate



urlpatterns = [
    path('virtual_items/', VirtualItemDetail.as_view(), name='virtualtem-detail'),
    path('virtual_items/<int:id>/', VirtualItemUpdate.as_view(), name='virtualitem-update'),
]





