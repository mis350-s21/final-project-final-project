from django.db import models

# Create your models here.
class Order(models.Model):

    STATUS = (
        (0, "Unconfirm"),
        (1, "confirm"),
    )

    item_name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    delivery_date= models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
     return f"{self.item_name}: created at {self.delivery_date}, cuctomer address {self.address}"
