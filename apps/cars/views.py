from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
