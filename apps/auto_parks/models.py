from django.db import models

from apps.users.models import UserModel

from core.models import BaseModel


class AutoParkModel(BaseModel):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=20)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')
