from django.db import models


# Create your models here.
class Author(models.Model):
    a_name=models.CharField(max_length=20)
    a_img=models.ImageField(upload_to='img')
    joined_date=models.DateField()
    country=models.CharField(max_length=20)

class Blog(models.Model):
    b_img=models.ImageField(upload_to='img')
    b_category=models.CharField(max_length=20)
    b_heading=models.TextField()
    name=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author_name',null=True,blank=True)
    img=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author_img',null=True,blank=True)
    b_posted_date=models.DateField(null=True,blank=True)
    b_desc=models.TextField(null=True,blank=True)


