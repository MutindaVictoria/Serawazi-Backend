

from django.urls import path
from .views import ScenariosDetailView,ScenariosListView
from .views import  VirtualItemDetail, VirtualItemUpdate
from .views import CategoryList, CategoryDetail,ScenarioCollectionListView,ScenarionCollectionDetailView,UserRegistrationListView
from api.views import UserLoginView,UserRegistrationView
urlpatterns = [

    path("gamers/register/", UserRegistrationView.as_view(), name="gamer-registration"),
    path("gamers/login/", UserLoginView.as_view(), name="gamer-login"),
    path("gamers/list/", UserRegistrationListView.as_view(), name="gamer-registration"),




    path("scenarios/", ScenariosListView.as_view(), name="scenarios_list_view"),
    path("scenarios/<int:id>/", ScenariosDetailView.as_view(), name="scenarios_detail_view"),
    path('scenario-collections/',ScenarioCollectionListView.as_view(), name='scenario-collection-list'),
    path('scenario-collections/<int:id>/',ScenarionCollectionDetailView.as_view(), name='scenario-collection-detail'),
    path('virtual_items/',VirtualItemDetail.as_view(), name='virtualtem-detail'),
    path('virtual_items/<int:id>/', VirtualItemUpdate.as_view(), name='virtualitem-update'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetail.as_view(), name='category-detail'),
]  



