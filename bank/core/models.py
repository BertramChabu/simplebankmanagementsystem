from django.db import models

# Create your models here.
# generate models for our system
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    ACCOUNT_TYPES = (
        ('SAVINGS', 'saving'),
        ('CURRENT', 'current'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_type =  models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customet.name} - {self.account_type} Account"

class Transactions(models.Model):
    TRANSACTION_TYPES = (
        ('DEPOSIT', 'deposit'),
        ('WITHDRAWAL', 'withdrawal')
    )
    account =  models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.cutomer.name} - {self.transaction_type} of {self.amount}"
    
