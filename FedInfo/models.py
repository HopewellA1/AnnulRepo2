from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Federation(models.Model):
    FedId = models.AutoField(primary_key=True,blank=False,null=False,auto_created=True)
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    FederationName = models.TextField(max_length=100)
    
    #ParentId = models.ForeignKey(Parent,blank=True,null=True,on_delete=models.CASCADE)
    #federation president info
    PresidentName = models.TextField(max_length=60)
    PresidentLastName = models.TextField(max_length=60)
    PresidentEmail = models.TextField(max_length=80)
    PresidentPhone = models.TextField(max_length=15)
    #Contact person info
    ContactPersonName = models.TextField(max_length=60)
    ContactPersonLastName = models.TextField(max_length=60)
    ContactPersonPosition = models.TextField(max_length=60)
    Email = models.TextField(max_length=80)
    
    Phone = models.TextField(max_length=15)
    AddedDate = models.DateTimeField() 
    yearUpdate = models.CharField(max_length=4)
    
    
class District(models.Model):
    DistrictId = models.AutoField(primary_key=True,blank=False,null=False,auto_created=True)
    Federation = models.ForeignKey(Federation,blank=True,null=True,on_delete=models.CASCADE)
    DistrictName = models.TextField(max_length=80)
    Participation = models.CharField(max_length=3,default="No")
    FormalStructure = models.CharField(max_length=3,default="No")
    ContactPersonName = models.TextField(max_length=80)
    ContactPersonLastName = models.TextField(max_length=80)
    Phone = models.TextField(max_length=15)
    Email = models.TextField(max_length=80)
    DistrictOrProvince = models.TextField(max_length=30)#Clubes register at District or province level
    NoStructureReason = models.TextField(default="Note stated",max_length=150)#Why they do not have a structur
    NumberOfClubs = models.IntegerField()
    AddDate = models.DateTimeField()
    
    
    
    
    
    