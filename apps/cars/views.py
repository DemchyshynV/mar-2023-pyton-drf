from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request

from apps.cars.filters import get_filtered_query_set
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return get_filtered_query_set(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
