from django.db import models
from django.contrib.auth.models import User
from product.models import Product



class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255, null=True, blank=True)
    shipping_zipcode = models.CharField(max_length=255,null=True, blank=True)
    shipping_country = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Shipping Address"
    
    def __str__(self):
        return f'Shipping Address - {str(self.id)}'
    

class Order (models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    order_shipping_address = models.TextField(max_length=1000)
    amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    date_shipped = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Order - {str(self.id)}'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)  
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'Order Item - {str(self.id)}'
