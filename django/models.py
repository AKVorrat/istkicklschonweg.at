
from django.db import models

class Signature(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    email = models.EmailField(max_length=256, unique=True)
    
    newsletter = models.BooleanField()
