from django.db import models
from urllib import request
from django.contrib.auth.models import User


class CarBrand(models.Model):
    name = models.CharField(max_length=60, unique=True)
    created_at = models.DateField(auto_now_add=True)
    deleted_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_brand = models.ForeignKey(
        CarBrand, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, unique=True)
    created_at = models.DateField()
    deleted_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class UserCar(models.Model):
    # user = models.CharField(max_length=60, unique=True)
    user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    # user_id = int(request.POST['id'])
    # user = request.POST['username']
    car_brand = models.ForeignKey(
        CarBrand, blank=True, null=True, on_delete=models.CASCADE)
    car_model = models.ForeignKey(
        CarModel, blank=True, null=True, on_delete=models.CASCADE)
    first_reg = models.DateField()
    odometer = models.IntegerField()
    created_at = models.DateField()
    deleted_at = models.DateField(blank=True, null=True)
