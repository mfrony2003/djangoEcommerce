from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(null=True,blank=True)
    is_subcategory = models.BooleanField(default=False,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)    
    category_id =  models.ForeignKey(Category,null=True,on_delete=models.CASCADE)   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):  
         return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    @property
    def shopurl(self):
        try:
            url =self.category_id.__str__()
        except:
            url = ''
        return url
        

    
class Order(models.Model):
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=True)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

class OrderProduct(models.Model):
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    order = models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    order = models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    


