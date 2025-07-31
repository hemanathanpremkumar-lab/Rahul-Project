from django.db import models

# Create your models here.
class Company(models.Model):
    Company_name=models.CharField(max_length=30)
    email=models.EmailField()
    Phone_no=models.CharField(max_length=20)
    X=models.URLField()
    facebook=models.URLField()
    instagram=models.URLField()
    linked_in=models.URLField()
    location=models.CharField(max_length=100,default='')
    open_days=models.CharField(max_length=20,default='Mon-Sat')
   
class Services(models.Model):
    icon=models.CharField(max_length=30)
    service_head=models.CharField(max_length=30)
    service_desc=models.TextField()

class Testimonals(models.Model):
    img=models.ImageField(upload_to='img')
    name=models.CharField(max_length=20)
    role=models.CharField(max_length=20)
    feedback=models.TextField()
    star=models.IntegerField(default=0)


class FAQ(models.Model):
    question=models.TextField()
    answer=models.TextField()

