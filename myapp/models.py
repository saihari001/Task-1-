from django.db import models

# Create your models here.
class SignUp(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    User_Type=models.CharField(max_length=20)
    Profile_Picture=models.ImageField(upload_to='media/profile_pic', null=True, blank=True)
    User_Name=models.CharField(max_length=50)
    Email_Id=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Address=models.TextField(max_length=100)