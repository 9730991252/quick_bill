from django.db import models

# Create your models here.
class Shope(models.Model):
    shope_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True)
    contact_details = models.CharField(max_length=500, null=True)
    pin = models.IntegerField()
    status = models.IntegerField(default=1)
    