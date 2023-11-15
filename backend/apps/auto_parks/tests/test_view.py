from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import AutoParkModel

UserModel = get_user_model()


class AutoParkTestCase(APITestCase):
    def _authenticate(self, admin=None):
        email = "admin@gmail.com"
        password = "P@$$word1"
        user = {
            "email": email,
            "password": password,
            "profile": {
                "name": "Іван",
                "surname": "Попов",
                "age": 18
            }
        }
        response = self.client.post(reverse('users_create'), user, format='json')
        user = UserModel.objects.get(email=email)
        if admin:
            user.is_staff = True
        user.is_active = True
        user.save()
        res = self.client.post(reverse('auth_login'), {'email': email, 'password': password})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {res.data["access"]}')

    def test_create_auto_park_without_auth(self):
        count = AutoParkModel.objects.count()
        sample_auto_park = {
            'name': 'Uber'
        }
        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEquals(AutoParkModel.objects.count(), count)

    def test_create_auto_park_without_admin(self):
        self._authenticate()
        count = AutoParkModel.objects.count()
        sample_auto_park = {
            'name': 'Uber'
        }
        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(AutoParkModel.objects.count(), count)

    def test_create_auto_park_with_admin(self):
        self._authenticate(admin=True)
        count = AutoParkModel.objects.count()
        sample_auto_park = {
            'name': 'Uber'
        }
        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(AutoParkModel.objects.count(), count+1)
