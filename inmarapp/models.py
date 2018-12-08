from django.db import models

# Create your models here.
class UserData(models.Model):           
    SKU = models.CharField(max_length=255)
    NAME = models.CharField(max_length=255)
    LOCATION = models.CharField(max_length=255)
    DEPARTMENT = models.CharField(max_length=255)
    CATEGORY = models.CharField(max_length=255)
    SUBCATEGORY = models.CharField(max_length=255)

    def __str__(self):
    	return '{}'.format(self.NAME)