from core.permissions import IsAdminWriteOrIsAuthenticatedRead
from drf_yasg.utils import swagger_auto_schema

from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
class CarListCreateView(ListCreateAPIView):
    """
        Get all cars
    """
    queryset = CarModel.my_objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    # permission_classes = (IsAdminWriteOrIsAuthenticatedRead,)
    permission_classes = (AllowAny,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get Car by ID
    put:
        Update car by ID
    patch:
        Partial update car by ID
    delete:
        Delete car by ID
    """
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminWriteOrIsAuthenticatedRead,)


class AddPhotoByCarIdView(UpdateAPIView):
    permission_classes = (IsAdminWriteOrIsAuthenticatedRead,)
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()
    http_method_names = ('put',)
    parser_classes= (MultiPartParser,)

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)
