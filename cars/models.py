from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    seats = models.IntegerField()
    body = models.CharField(max_length=10)
    engine_volume = models.FloatField()
