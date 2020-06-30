from django.db import models
from django.db import connections

# Create your models here.

class Test(models.Model):
    name =  models.CharField('name', max_length=50)
    test =  models.CharField('test', max_length=50)
    roll =  models.CharField('roll', max_length=20)


    class Meta:
        managed = False
        db_table = 'test'

