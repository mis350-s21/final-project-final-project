from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image=models.CharField(max_length=300)
    # notes=models.TextField()
    
    


    def __str__(self):
        return f"{self.title}"
 
class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
 
class Payment(models.Model):
    METHOD = (
        (0, "Master Card"),
        (1, "Cash"),
    )

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    method = models.IntegerField(choices=METHOD, default=0)


class Comments(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"{self.name}"



#class User(models.Model):
  #  mobile = models.BigIntegerField()