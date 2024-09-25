from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='uploads/product/') 
    description = models.CharField(max_length= 300, default='', blank=True, null= True,)
    #add sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone= models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=20, default='', blank=True)
    date =  models.DateField(default= datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
