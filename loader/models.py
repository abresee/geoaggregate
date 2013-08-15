from django.contrib.gis.db import models
class Region(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=255)

class StateEquiv(Region):
    def __str__(self):
        return self.name

class CountyEquiv(Region):
    parent = models.ForeignKey('StateEquiv')

    def __str__(self):
        return self.name + ', ' + self.parent.name
