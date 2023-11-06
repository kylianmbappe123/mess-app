from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_mess=models.BooleanField(default=False,verbose_name='is mess')
    is_custumer=models.BooleanField(default=False,verbose_name='is customer')
    name=models.CharField(max_length=100,default='user')
    mobile_number=models.CharField(max_length=20,default='nil')
    bank_name=models.CharField(max_length=100,default='nil')
    bank_account_number=models.CharField(max_length=50,default='nil')
    ifsc_code=models.CharField(max_length=20,default='nil')
    upi_id=models.CharField(max_length=100,default='nil')
    profile_picture=models.ImageField(upload_to='profile_picture',blank=True,null=True)
    location=models.CharField(max_length=300, default='nil')
    address=models.TextField(max_length=1000,default='nil')
    district=models.CharField(max_length=150,default='nil')

    def __str__(self):
        return self.username
        