from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# from cars.models import CarModel
from .models import CarModel
from django.forms import model_to_dict
from .serializers import CarSerializer
from rest_framework import status

# class TestOneView(APIView):
#     def get(self, *args, **kwargs):
#         return Response('hello from get')
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         print(data)
#         params_dict = self.request.query_params.dict()
#         print(params_dict)
#         return Response('hello from post')
#
#     def put(self, *args, **kwargs):
#         return Response('hello from put')
#
#     def patch(self, *args, **kwargs):
#         return Response('hello from patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('hello from delete')
#
#
# class TestTwoView(APIView):
#     def get(self,*args, **kwargs):
#         print(kwargs)
#         return Response('ok')

class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        # res = [model_to_dict(car) for car in cars]
        serializer = CarSerializer(cars, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        # car = CarModel.objects.create(**data)
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()

        # serializer_data = serializer.data
        # print(serializer_data)
        # car = CarModel(**serializer_data)
        # car.save()
        # car_serializer = CarSerializer(car)
        # res = model_to_dict(car)
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        # res = model_to_dict(car)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serializer = CarSerializer(car, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serializer = CarSerializer(car, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            raise Http404()

        return Response(status=status.HTTP_204_NO_CONTENT)