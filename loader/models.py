from django.contrib.gis.db import models

class StateEquiv(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class CountyEquiv(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('StateEquiv')
    def __str__(self):
        return self.name + ', ' + self.parent.name
