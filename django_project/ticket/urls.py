from django.urls import path
from . import views

urlpatterns = [
    path('create-ticket/', views.create_ticket, name='create-ticket'),
    path('customer-active-tickets/', views.customer_active_tickets, name='customer-active-tickets'),
    path('customer-resolved-tickets/', views.customer_resolved_tickets, name='customer-resolved-tickets'),
    path('assign-ticket/<str:ticket_id>/', views.assign_ticket, name='assign-ticket'),
    path('ticket-details/<str:ticket_id>/', views.ticket_details, name='ticket-details'),
    path('ticket-queue/', views.ticket_queue, name='ticket-queue'),
]