from django.urls import path
from .views import VirtualItemCreate, VirtualItemDelete, VirtualItemDetail ,VirtualItemUpdate ,VirtualItemList

urlpatterns = [
    path('virtual_items/', VirtualItemList.as_view(), name='virtual_item_list'),
    path('virtual_items/<int:id>/', VirtualItemDetail.as_view(), name='virtual_item_detail'),
    path('virtual_items/create/', VirtualItemCreate.as_view(), name='virtual_item_create'),
    path('virtual_items/update/<int:id>/', VirtualItemUpdate.as_view(), name='virtual_item_update'),
    path('virtual_items/delete/<int:id>/', VirtualItemDelete.as_view(), name='virtual_item_delete'),
]