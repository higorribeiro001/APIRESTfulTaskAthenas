from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    date_birth = models.DateField(null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True)
    sex = models.CharField(max_length=1, null=False, blank=False)
    height = models.FloatField(null=False, blank=False)
    weight = models.FloatField(null=False, blank=False)