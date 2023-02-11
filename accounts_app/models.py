from asyncio.windows_events import NULL
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fathers_name=models.CharField(max_length=50,unique=True)
    nationalcod=models.CharField(max_length=10)
    image=models.ImageField(upload_to='profile/image',null=True , blank=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name='حساب کاربری'
        verbose_name_plural='حساب های کاربری'
    
    