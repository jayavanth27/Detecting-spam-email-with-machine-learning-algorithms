from django.db import models

# Create your models here.

class OAuth(models.Model):
    emailId = models.CharField(max_length=100)
    otp = models.IntegerField()