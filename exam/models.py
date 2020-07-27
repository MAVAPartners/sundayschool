from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    #is_approved = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
'''
class UserType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

'''    

class School(models.Model):
    """ School Model """
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    """ Student Model """
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school')
    gender = models.CharField(max_length=10, default='')
    age = models.IntegerField( default=0)
    address = models.CharField(max_length=255, default='')
    address2 = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    zipcode = models.IntegerField( default=0)
    phoneno = models.CharField( default='', max_length=15,)
    score = models.IntegerField(default=0)
    accademicYear = models.IntegerField( default=0)
    is_approved = models.BooleanField(default=False)
    status = models.IntegerField( default=0)

    def __str__(self):
        return self.user.username
