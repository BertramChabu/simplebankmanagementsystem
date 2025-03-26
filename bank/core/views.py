from django.shortcuts import render, redirect
from .models import Account, Customer, Transactions
from .serializer import AccountSerializer, CustomerSerializer, TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import CustomerForm
# Customer API
api_view(['GET'])
def viewCustomers(request):
    data= Customer.objects.all()
    customers= CustomerSerializer(data, many=True).data
    return render(request, "customer.html", {"customers": customers})

api_view(['POST'])
def addCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer.html')
    else:
        form = CustomerForm()

    return render(request, 'customer.html', {'form': form})

