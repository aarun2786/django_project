from django.db import models

# Create your models here.
class User_data(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class User_info(models.Model):
    user = models.OneToOneField(User_data,on_delete=models.CASCADE)
    dob = models.DateField()
    phone_no = models.CharField(max_length=12)

