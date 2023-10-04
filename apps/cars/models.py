from datetime import datetime

from django.db import models

from core.models import BaseModel
from django.core import validators as V


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    # brand = models.CharField(max_length=25, unique=True)
    # brand = models.CharField(max_length=25, null=True)
    # brand = models.CharField(max_length=25, blank=True)
    brand = models.CharField(max_length=25, validators=[V.MinLengthValidator(3), V.MinLengthValidator(25)])
    # price = models.IntegerField(default=0)
    price = models.IntegerField(validators=[V.MaxValueValidator(1000000), V.MinValueValidator(0)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)])
