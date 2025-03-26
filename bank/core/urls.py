from django.urls import path
from .views import viewCustomers, addCustomer
urlpatterns =[
    path('customers/', viewCustomers),
    path('customers/add_customer/', addCustomer)
]
