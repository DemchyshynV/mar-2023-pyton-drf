from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from .views import ActivateUserView, MeView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/me', MeView.as_view(), name='auth_me'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='auth_activate_user')
]