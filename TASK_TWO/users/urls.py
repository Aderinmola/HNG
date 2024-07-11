from django.urls import path
from .views import UserCreateView, LoginView, GetUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #  /auth/register
    path('auth/register/', UserCreateView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    # /api/users/:id :
    path('api/users/<str:pk>/', GetUserView.as_view(), name='get_user'),
]



