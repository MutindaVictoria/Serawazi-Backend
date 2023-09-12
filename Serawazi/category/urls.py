from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),
=======
from .views import CategoryList, CategoryDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetail.as_view(), name='category-detail'),
>>>>>>> 94138d22fc74e82a1495a31cee23f19c2fbd1054
]
