from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user=models.CharField(max_length=32)
    word=models.CharField(max_length=100)
    Time=models.CharField(max_length=32)
