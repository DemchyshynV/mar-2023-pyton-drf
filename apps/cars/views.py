from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, GenericAPIView
from .filters import car_filtered_queryset
from .models import CarModel
from django.forms import model_to_dict
from .serializers import CarSerializer
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CarListCreateView(ListCreateAPIView):
    # queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

# class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     serializer_class = CarSerializer
#
#     def get_queryset(self):
#         return car_filtered_queryset(self.request.query_params)
#
#     # def perform_create(self, serializer):
#     #
#     #     serializer.save
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
#
#     # def get(self, *args, **kwargs):
#     #     # qs = CarModel.objects.filter(price__gte=1000).exclude(brand='oka')
#     #     # qs = CarModel.objects.all().order_by('-price', '-brand').reverse()
#     #     # qs = CarModel.objects.filter(price__lte=100)
#     #     # qs = qs.filter(price__gte=1000)
#     #
#     #     # qs = CarModel.objects.filter(Q(brand='oka') | Q(price=500))
#     #     # print(qs.query)
#     #
#     #     # cars = CarModel.objects.all().values('brand', 'price')
#     #     # cars.filter(brand='oka')
#     #     # print(cars[0].__dict__)
#     #     # print(qs_filter.query)
#     #
#     #     # return Response(serializer.data, status.HTTP_200_OK)
#     #
#     #     # cars = CarModel.objects.all()[:4:2]
#     #     # cars = cars.filter(price__gt=1000)
#     #     # get = CarModel.objects.get(brand='kia')
#     #     # CarModel.objects.all().get()
#     #     cars = car_filtered_queryset(self.request.query_params)
#     #     serializer = CarSerializer(cars, many=True)
#     #     return Response(serializer.data, status.HTTP_200_OK)
#
#     # def post(self, *args, **kwargs):
#     #     data = self.request.data
#     #     serializer = CarSerializer(data=data)
#     #
#     #     if not serializer.is_valid():
#     #         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#     #
#     #     serializer.save()
#     #
#         # return Response(serializer.data, status.HTTP_201_CREATED)
#
#
#
# # class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
# #     pass
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get_object(self):
#         return CarModel.objects.get(brand='kia')
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
#
#     # lookup_field = 'my'
#     # lookup_url_kwarg = 'my'
#
#     def get(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#         # car = get_object_or_404(CarModel, pk=pk
#         car = self.get_object()
#         serializer = self.get_serializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#         try:
#             car = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             raise Http404()
#         serializer = CarSerializer(car, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#         try:
#             car = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             raise Http404()
#         serializer = CarSerializer(car, data=data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs['pk']
#         try:
#             car = CarModel.objects.get(pk=pk)
#             car.delete()
#         except CarModel.DoesNotExist:
#             raise Http404()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)
