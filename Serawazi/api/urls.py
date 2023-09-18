# from django.urls import path
# from .views import AdminListView, AdminDetailView, AdminRegistrationView, AdminLoginView
# from .views import RegularUserListView, RegularUserDetailView, RegularUserRegistrationView, RegularUserLoginView
# from .views import ScenariosListView, ScenariosDetailView 




# urlpatterns = [
#     # path("user_registrations/", User_RegistrationListView.as_view(), name="user_registration_list_view"),
#     # path("user_registrations/<int:id>/", User_RegistrationDetailView.as_view(), name="user_registration_detail_view"),

#     # path("login/", LoginListView.as_view(), name="login_list_view"),
#     # path("login/<int:id>/", LoginDetailView.as_view(), name="login_detail_view"),
    
#     path("scenarios/", ScenariosListView.as_view(), name="scenarios_list_view"),
#     path("scenarios/<int:id>/", ScenariosDetailView.as_view(), name="scenarios_detail_view"),

#     path('admins/',AdminListView.as_view(), name= "admin-list"),
#     path('admins/<int:id>/',AdminDetailView.as_view(), name= "admin-detail"),
#     path('admins/register/',AdminRegistrationView.as_view(), name= "admin-register"),
#     path('admins/login/',AdminLoginView.as_view(), name='admin-login'),
#     # RegularUser
#     path('regularusers/',RegularUserListView.as_view(), name='regularuser-list'),
#     path('regularusers/<int:id>/',RegularUserDetailView.as_view(), name='regularuser-detail'),
#     path('regularusers/register/',RegularUserRegistrationView.as_view(), name='regularuser-register'),
#     path('regularusers/login/',RegularUserLoginView.as_view(), name='regularuser-login'),
# ]





from django.urls import path
from .views import CustomUserListView,CustomUserDetailView,AdminsRegistrationView,AdminsLoginView,GamerRegistrationView,GamerLoginView,ScenariosDetailView,ScenariosListView

urlpatterns = [
    path("users/",CustomUserListView.as_view(), name="user-list"),
    path("users/<int:id>/", CustomUserDetailView.as_view(), name="user-detail"),
    path("admins/register/", AdminsRegistrationView.as_view(), name="admins-registration"),
    path("admins/login/", AdminsLoginView.as_view(), name="admins-login"),
    path("gamers/register/", GamerRegistrationView.as_view(), name="gamer-registration"),
    path("gamers/login/", GamerLoginView.as_view(), name="gamer-login"),


    path("scenarios/", ScenariosListView.as_view(), name="scenarios_list_view"),
    path("scenarios/<int:id>/", ScenariosDetailView.as_view(), name="scenarios_detail_view"),
]  
