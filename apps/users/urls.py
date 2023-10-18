from django.urls import path

from .views import UserAddAvatarView, UserCreateView

urlpatterns = [
    path('', UserCreateView.as_view(), name='users_create'),
    path('/avatars', UserAddAvatarView.as_view(), name='users_add_avatar')
]
