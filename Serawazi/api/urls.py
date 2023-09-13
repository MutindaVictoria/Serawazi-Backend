from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.ScenarioCollectionListView.as_view(), name='message-list'),
    path('collections/<int:id>/', views.ScenarionCollectionDetailView.as_view(), name='message-detail'),
]
