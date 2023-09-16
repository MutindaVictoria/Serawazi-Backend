from django.urls import path
from . import views

urlpatterns = [
    path('scenario-collections/', views.ScenarioCollectionListView.as_view(), name='scenario-collection-list'),
    path('scenario-collections/<int:id>/', views.ScenarionCollectionDetailView.as_view(), name='scenario-collection-detail'),
]
