from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.request import Request

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer

from core.permissions import IsAdminWriteOrIsAuthenticatedRead, IsSuperUser


class CarListCreateView(ListAPIView):
    queryset = CarModel.my_objects.cars_audi()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    permission_classes = (IsAdminWriteOrIsAuthenticatedRead,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminWriteOrIsAuthenticatedRead,)


class AddPhotoByCarIdView(UpdateAPIView):
    permission_classes = (IsAdminWriteOrIsAuthenticatedRead,)
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()
    http_method_names = ('put',)

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)
