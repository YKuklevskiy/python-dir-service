from django.db import models

# Create your models here.
class Entry(models.Model):

    station = models.CharField("station", max_length=100, null=True)
    line = models.CharField("station", max_length=100, null=True)
    admin_area = models.CharField("station", max_length=100, null=True)
    district = models.CharField("station", max_length=100, null=True)
    status = models.CharField("station", max_length=100, null=True)
    entryID = models.IntegerField("station", null=True)

    def __str__(self):
        return self.station
