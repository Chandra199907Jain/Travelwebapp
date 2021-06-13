from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length = 200)
    email = models .CharField(max_length = 200)
    mobile = models.IntegerField()
    password = models.CharField(max_length = 200)
    
