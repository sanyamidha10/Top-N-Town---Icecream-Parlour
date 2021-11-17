from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122, default='')
    email = models.CharField(max_length=122,default='')
    phone = models.CharField(max_length=12,default='')
    desc = models.TextField(max_length=150,default='')
    
    def __str__(self) -> str:
        return self.name