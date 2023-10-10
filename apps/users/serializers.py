from rest_framework import serializers

from apps.auto_parks.serializers import AutoParkWithOutCarsSerializer
from apps.users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    auto_parks = AutoParkWithOutCarsSerializer(read_only=True, many=True)

    class Meta:
        model = UserModel
        fields = ('id', 'name', 'age', 'created_at', 'updated_at', 'auto_parks')
