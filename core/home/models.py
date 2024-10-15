from django.db import models

from django.db.models.signals import post_save, pre_save, post_delete,pre_delete
from django.dispatch import receiver
from django.utils.text import slugify

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True,blank=True)
    image = models.ImageField()
    file = models.FileField()

class Car(models.Model):
    car_name = models.CharField(max_length=20)
    type = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.car_name} - {self.type}"
    
@receiver(post_save, sender=Car)     # it call when above Car object is created
def call_car_api(sender, instance, **kwargs):
    print('\n\nCar object created \n\n')
    print(sender)
    print("-")
    print(instance)
    print("-")
    print(kwargs)

@receiver(pre_save, sender=Car)
def pre_save_car(sender, instance, **kwargs):
    # Automatically generate a slug for the car name before saving
    instance.slug = slugify(instance.car_name)
    print(f"Slug generated for {instance.car_name}: {instance.slug}")