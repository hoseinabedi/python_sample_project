from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True)
    joined_date = models.DateTimeField(null=True)