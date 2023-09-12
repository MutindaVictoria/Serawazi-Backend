from django.urls import path
from .views import MessageListView, MessageDetailView
urlpatterns = [ 
path('messages/', MessageListView.as_view(), name='message_list_view'), 
path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail_view'), 
]