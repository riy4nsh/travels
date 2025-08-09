from django.db import models



# Create your models here.
class registertbl(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    repeatpassword=models.CharField(max_length=100)

    class Meta:
        db_table="registertbl"

class contacttbl(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    class Meta:
        db_table="contacttbl"

class logintbl(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table="logintbl"
