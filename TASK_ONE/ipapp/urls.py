# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import IpappViewSet


# router = DefaultRouter()
# router.register(r'ipapp', IpappViewSet)

# urlpatterns = [
#     path('', include(router.urls)),

# ]

from django.urls import path
from .views import IpappViewSet

urlpatterns = [
    path('hello/', IpappViewSet.as_view(), name='hello'),
]
