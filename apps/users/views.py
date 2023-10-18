from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.users.serializers import ProfileAvatarSerializer, UserSerializer

from core.dataclasses.user_dataclass import ProfileDataClass
from core.permissions import IsAdminOrWriteOnly, IsSuperUser

UserModel = get_user_model()


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrWriteOnly,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)


class UserAddAvatarView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileAvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return UserModel.objects.get(pk=self.request.user.pk).profile

    def perform_update(self, serializer):
        profile:ProfileDataClass = self.get_object()
        profile.avatar.delete()
        super().perform_update(serializer)



