from django.db import models

# Create your models here.
# CRUD
'''

CREATE AN OBJECT

Car.objects.create(car_name = "BMW",speed=100)

car_dict = {"car_name":"Alto","speed":50}
Car.objects.create(**car_dict)

car = Car(car_name = "nexon", speed = 100)
car.save()

_____________________________________________________________

READ AN OBJECT

car = Car.objects.filter(id = 1)

_____________________________________________________________

UPDATE AN OBJECT

car = Car.objects.get(id = 1) select the object
car = Car.car_name = "Mercedy"
car.speed = 170
car.save()

car = Car.objects.filter(id = 1).update(car_name = "Toyota")

_____________________________________________________________

DELETE AN OBJECT

Car.objects.all().delete()      # Delete all data

Car.objects.get(id = 1).delete()   # Only delete id 1 record

'''

class Student(models.Model):
   # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField()

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self) ->str:
        return self.car_name
