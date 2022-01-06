from django.db import models

# Create your models here.
class Products(models.Model):
    item_name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image=models.CharField(max_length=300)
    # notes=models.TextField()

    def __str__(self):
        return f"{self.item_name}"