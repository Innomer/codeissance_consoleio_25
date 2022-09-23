from django.db import models

# Create your models here.
class Profile(models.Model):
    pp=models.ImageField(null=True)
    username=models.CharField(max_length=20,blank=True)
    fullname=models.CharField(max_length=50,blank=True)
    ed=models.CharField(max_length=40,blank=True,null=True)
    abt=models.TextField(max_length=200,blank=True,null=True)
    bday=models.DateField(null=True)
    city=models.CharField(max_length=20,blank=True,null=True)
    country=models.CharField(max_length=20,blank=True,null=True)
    career=models.CharField(max_length=50,blank=True,null=True)
    interest=models.JSONField(default=list,null=True)
    communities=models.JSONField(default=list,null=True)
    streak=models.IntegerField(null=True)
    pw=models.CharField(max_length=16,blank=False,default='djangotest')
    email=models.EmailField(max_length=254,default="xyz")
    token=models.IntegerField(null=True,blank=True)

class Community(models.Model):
    cName=models.CharField(max_length=50,blank=True,null=True)
    noMem=models.IntegerField(null=True)
    
    