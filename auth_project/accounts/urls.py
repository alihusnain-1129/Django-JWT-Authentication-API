from django.urls import path
from .views import ChangePasswordView, ProtectedView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]