# Import your views and necessary modules
from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the list and create view
    path('collections/', views.ScenarioCollectionListCreateView.as_view(), name='scenario-collection-list-create'),

    # URL pattern for the retrieve, update, and delete view
    path('collections/<int:id>/', views.ScenarioCollectionRetrieveUpdateDestroyView.as_view(), name='scenario-collection-retrieve-update-destroy'),
]
