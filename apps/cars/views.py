from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.my_objects.cars_audi()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
