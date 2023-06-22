from django.db import models

# Create your models here.
class steregistration(models.Model):
    stdid=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    age=models.IntegerField()
    mobile=models.IntegerField()
    email=models.CharField(max_length=20)
# Create your models here.
class studentfer(models.Model):
    stdudeid=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    age=models.IntegerField()
    mobile=models.IntegerField()
    email=models.CharField(max_length=20)
    fullmarks=models.IntegerField()
    obtaindmarks=models.IntegerField()
    grad=models.CharField(max_length=20)
    percentage=models.CharField(max_length=20)
    attendance=models.CharField(max_length=20)
    studenttype=models.CharField(max_length=20)
    performance=models.CharField(max_length=20)
    studeimage=models.ImageField()