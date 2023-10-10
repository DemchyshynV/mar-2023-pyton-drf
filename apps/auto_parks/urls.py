from django.urls import path

from apps.auto_parks.views import AutoParkListCreateCarView, AutoParkListCreateView, AutoParkRetrieveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_parks_list_create'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view(), name='auto_park_retrieve_update_destroy'),
    path('/<int:pk>/cars', AutoParkListCreateCarView.as_view(), name='auto_parks_add_car')

]
