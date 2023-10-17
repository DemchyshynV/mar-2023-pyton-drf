from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return (IsAuthenticated(),)
        return (AllowAny(),)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

# class UserListView(ListAPIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         return UserModel.objects.exlude(pk=self.request.user.pk)
