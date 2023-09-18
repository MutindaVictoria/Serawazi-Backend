from django.urls import path
# from . import views
from .views import  VirtualItemDetail, VirtualItemUpdate
from .views import CategoryList, CategoryDetail,ScenarioCollectionListView,ScenarionCollectionDetailView

urlpatterns = [
    path('scenario-collections/',ScenarioCollectionListView.as_view(), name='scenario-collection-list'),
    path('scenario-collections/<int:id>/',ScenarionCollectionDetailView.as_view(), name='scenario-collection-detail'),
    path('virtual_items/',VirtualItemDetail.as_view(), name='virtualtem-detail'),
    path('virtual_items/<int:id>/', VirtualItemUpdate.as_view(), name='virtualitem-update'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetail.as_view(), name='category-detail'),
]
