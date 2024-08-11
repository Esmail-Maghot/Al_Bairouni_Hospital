from django.db import models

# Create your models here.

class Sections(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    #doctors=
    #patients=

    def __str__(self):
        return self.name


class Doctors(models.Model):
    name = models.CharField(max_length=25)
    phone= models.CharField(max_length=10, blank=True)
    #section=
    #patients=
    
    def __str__(self):
        return self.name


class Patients(models.Model):
    id_num= models.CharField(max_length=11, unique=True, null=True)
    name = models.CharField(max_length=50)
    mother_name= models.CharField(max_length=25, default="")
    gender= models.TextChoices("Male", "Female")
    phone= models.CharField(max_length=10, unique=True)
    address= models.CharField(max_length=100)
    #birth_date= 
    #section=
    #doctor=

    def __str__(self):
        return self.name


class Patient_Record(models.Model):
    record_id= models.CharField(max_length=20, unique=True)
    create= models.DateTimeField(auto_now_add=True)
    update= models.DateTimeField(auto_now=True)
    Patient_name= models.CharField(max_length=25)
    doctor_name= models.CharField(max_length=25)
    #section=
