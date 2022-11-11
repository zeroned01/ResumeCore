from django.db import models

# Create your models here.

class Contect(models.Model):
    name=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    qerry=models.CharField(max_length=100)