from django.db import models

# Create your models here.
class Profile(models.Model):
    pp=models.FileField(null=True)
    username=models.CharField(max_length=20,blank=True)
    fullname=models.CharField(max_length=50,blank=True)
    ed=models.CharField(max_length=40,blank=True,null=True)
    abt=models.TextField(max_length=200,blank=True,null=True)
    bday=models.CharField(max_length=10,null=True,blank=True)
    city=models.CharField(max_length=20,blank=True,null=True)
    country=models.CharField(max_length=20,blank=True,null=True)
    career=models.CharField(max_length=50,blank=True,null=True)
    interest1=models.CharField(max_length=50,blank=True,null=True)
    interest2=models.CharField(max_length=50,blank=True,null=True)
    interest3=models.CharField(max_length=50,blank=True,null=True)
    communities1=models.CharField(max_length=50,blank=True,null=True)
    communities2=models.CharField(max_length=50,blank=True,null=True)
    communities3=models.CharField(max_length=50,blank=True,null=True)
    streak=models.IntegerField(null=True)
    pw=models.CharField(max_length=16,blank=False,default='djangotest')
    email=models.EmailField(max_length=254,default="xyz")
    token=models.IntegerField(null=True,blank=True)
    activeChat1=models.IntegerField(null=True,blank=True)
    activeChat2=models.IntegerField(null=True,blank=True)
    comChat1=models.IntegerField(null=True,blank=True)
    comChat2=models.IntegerField(null=True,blank=True)

class Community(models.Model):
    cName=models.CharField(max_length=50,blank=True,null=True)
    noMem=models.IntegerField(null=True)
    
    