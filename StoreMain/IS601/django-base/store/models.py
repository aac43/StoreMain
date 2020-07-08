from django.db import models

class StoreGood(models.Model):
    OrderDate = models.DateField()
    CustomerID = models.CharField(max_length=25)
    Category = models.TextField()
    Sales = models.DecimalField(max_digits=6, decimal_places=2)
    ProductName = models.TextField()
    CustomerName = models.CharField(max_length=64)
    State = models.CharField(max_length=25)