from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    date = models.DateField()
    