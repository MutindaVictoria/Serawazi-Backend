from django.urls import path
from .views import User_RegistrationListView, User_RegistrationDetailView  
from .views import ScenariosListView, ScenariosDetailView  

urlpatterns = [
    path("user_registrations/", User_RegistrationListView.as_view(), name="user_registration_list_view"),
    path("user_registrations/<int:id>/", User_RegistrationDetailView.as_view(), name="user_registration_detail_view"),
    path("scenarios/", ScenariosListView.as_view(), name="scenarios_list_view"),
    path("scenarios/<int:id>/", ScenariosDetailView.as_view(), name="scenarios_detail_view"),
]
