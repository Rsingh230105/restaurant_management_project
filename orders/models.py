from django.db import models
from django.conf import settings
# Create your models here.

class OrderStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class order(models.Model):
    status = models.ForeignKey(OrderStatus,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"Order {self.id}"