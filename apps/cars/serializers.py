from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body','created_at', 'updated_at')

    # def validate_brand(self, brand):
    #     if brand == 'Sas':
    #         raise serializers.ValidationError({'detail': 'brand == Sas'})
    #     return brand
    #
    # def validate(self, attrs):
    #     price = attrs['price']
    #     year = attrs['year']
    #     if price == year:
    #         raise serializers.ValidationError({'detail': 'year==price'})
    #     return attrs
