from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class  Profiles(models.Model):
    users=models.OneToOneField(User,on_delete=models.CASCADE)
    Country=models.CharField(max_length=255,null=True)
    City=models.CharField(max_length=255,null=True)
    
    Photo=models.ImageField(upload_to='photoUser/',null=True)
    Phone=models.CharField(max_length=255,null=True)
    
    def __str__(self) -> str:
        return self.users.username

