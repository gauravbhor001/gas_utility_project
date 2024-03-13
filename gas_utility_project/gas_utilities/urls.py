from django.urls import path
from .views import create_service_request, ServiceRequestListView, ServiceRequestDetailView

urlpatterns = [
    path('create/', create_service_request, name='create_service_request'),
    path('list/', ServiceRequestListView.as_view(), name='service_request_list'),
    path('detail/<int:pk>/', ServiceRequestDetailView.as_view(), name='service_request_detail'),
]
