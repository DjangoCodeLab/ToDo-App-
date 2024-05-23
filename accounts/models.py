from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_account(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null= True)
    date_of_birth = models.DateField(blank=True, null = True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True,null = True)
    

    def __str__(self):
        return self.user.username
    

    

