from django.db import models

        
class Customer(models.Model):
    Name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    Phone = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
class Tags(models.Model):
    Name = models.CharField(max_length=200,null=True)
     
    def __str__(self):
        return self.Name        

class Product(models.Model):
    CATEGORY = (('Indoor','Indoor'),('Out Door','Out Door'),)
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags)

    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (('pending','pending'),('Out For Delivery','Out For Delivery'),('Delivered','Delivered'))
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    

