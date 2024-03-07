from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    permission = models.BooleanField(default=False)

class UAV(models.Model):
    serial = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    ammo = models.ForeignKey('Ammo', on_delete=models.CASCADE)
    weight = models.CharField(max_length=100)

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name


class Model(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=100)

    def __str__(self):
        return self.model_name

class Ammo(models.Model):
    ammo_id = models.AutoField(primary_key=True)
    ammo_name = models.CharField(max_length=100)

    def __str__(self):
        return self.ammo_name

class Rent(models.Model):
    rent_no = models.AutoField(primary_key=True)
    rented_uav_serial = models.ForeignKey('UAV', on_delete=models.CASCADE)
    who_rent = models.ForeignKey('User', on_delete=models.CASCADE)
    rent_date_start = models.DateTimeField()
    rent_date_end = models.DateTimeField()