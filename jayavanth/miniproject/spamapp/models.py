from django.db import models

# Create your models here.
class spammail(models.Model):
    Email_Body=models.CharField(max_length=100,default='')
    timestamp=models.DateTimeField()
    class Meta():
       ordering=[('-timestamp')]