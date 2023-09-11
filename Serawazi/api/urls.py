# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.ScenarioCollectionListCreateView.as_view(), name='collection-list-create'),
    path('collections/<int:pk>/', views.ScenarioCollectionRetrieveUpdateDestroyView.as_view(), name='collection-detail'),
]
