from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework import serializers
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class QuerySerializer(serializers.Serializer):
    price_lt = serializers.IntegerField()
    price_lte = serializers.IntegerField()
    price_gt = serializers.IntegerField()
    price_gte = serializers.IntegerField()
    year_lt = serializers.IntegerField()
    year_lte = serializers.IntegerField()
    year_gt = serializers.IntegerField()
    year_gte = serializers.IntegerField()
    brand_start = serializers.CharField()
    brand_end = serializers.CharField()
    brand_cont = serializers.CharField()
    order = serializers.CharField()


def get_filtered_query_set(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    serializer = QuerySerializer(data=query, partial=True)
    serializer.is_valid(raise_exception=True)

    for k, v in serializer.validated_data.items():
        match k:
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)

            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)
            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)

            case 'brand_start':
                qs = qs.filter(brand__startswith=v)
            case 'brand_end':
                qs = qs.filter(brand__endswith=v)
            case 'brand_cont':
                qs = qs.filter(brand__contains=v)

            case 'order':
                fields = CarSerializer.Meta.fields
                fields = [*fields, *[f'-{field}' for field in fields]]
                if v not in fields:
                    raise serializers.ValidationError({'detail': f'Please order choice from: {" , ".join(fields)}'})
                qs = qs.order_by(v)

    return qs
