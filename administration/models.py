from django.db import models

# Create your models here.
class employeeregistration(models.Model):
    stdid=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    workrole=models.CharField(max_length=20)
    emp_name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    age=models.IntegerField()
    mobile=models.IntegerField()
    email=models.CharField(max_length=20)
#models for employee selary 
class empselary2(models.Model):
    employee_id=models.CharField(max_length=20,primary_key=True)
    employee_name=models.CharField(max_length=20)
    employee_address=models.CharField(max_length=20)
    employee_total_income=models.IntegerField()
    date=models.CharField(max_length=20)
    employee_monthely_income=models.IntegerField()
    employee_total_income=models.IntegerField()
    employee_given_income=models.IntegerField()
    employee_remaning_income=models.IntegerField()
    employee_role=models.CharField(max_length=20)
#models for student fees form 
class studentfees(models.Model):
    studid=models.CharField(max_length=20,primary_key=True)
    student_name=models.CharField(max_length=20)
    student_address=models.CharField(max_length=20)
    student_course=models.CharField(max_length=20)
    admision_date=models.CharField(max_length=20)
    total_fees=models.IntegerField()
    given_fees=models.IntegerField()
    remaning_fees=models.IntegerField()
    course_duration=models.CharField(max_length=20)
#-----------------------------------------------------------
#models for idcard generating 
class idcardgenerate(models.Model):
    idcard_number=models.CharField(max_length=20,primary_key=True)
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
#---------------------------------------------------------------
# models for admin registration
class adminregistration(models.Model):
    admin_id=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    workrole=models.CharField(max_length=20)
    admin_name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    age=models.IntegerField()
    mobile=models.IntegerField()
    email=models.CharField(max_length=20)
#---------------------------------------------------------------------
class emprofile(models.Model):
    employees_id=models.CharField(max_length=20,primary_key=True)
    employee_name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    email_id=models.CharField(max_length=20)
    age=models.IntegerField()
    mobile=models.IntegerField()
    teaching_subject=models.CharField(max_length=20)
    presinting=models.CharField(max_length=20)
    performance=models.CharField(max_length=20)
    emplimage=models.ImageField()

    