from datetime import datetime

from django.core import validators as V
from django.db import models

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices.body_type_choices import BodyTypeChoices

from core.enums.regex_enum import RegEx
from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ['-id']

    brand = models.CharField(max_length=20, validators=[V.RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.msg)])
    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1000000)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)])
    body = models.CharField(max_length=9, choices=BodyTypeChoices.choices)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
