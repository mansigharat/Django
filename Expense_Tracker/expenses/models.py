from django.db import models

# Create your models here.
class Expense(models.Model):
    
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    date = models.DateField()