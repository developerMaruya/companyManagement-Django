from django.db import models

# Create your models here.
class idfetch(models.Model):
    idno=models.CharField(max_length=20,primary_key=True)
    role=models.CharField(max_length=20)
#---------------------------------------------------------
#models for enquari data
class enquari1(models.Model):
    course=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email=models.CharField(max_length=20)
#models for idcard generating 
class idgenerate1(models.Model):
    idcard_number=models.CharField(max_length=20,primary_key=True)
    user_password=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    mobile=models.IntegerField()
    qualification=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    age=models.IntegerField()
    session=models.CharField(max_length=20)
    role=models.CharField(max_length=20)