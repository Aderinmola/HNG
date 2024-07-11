from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import AddUserSerializer, LoginSerializer, GetUserSerializer
from django.contrib.auth import get_user_model
# from ..organisation.models import Organisation

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AddUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = AddUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "status": "success",
                "message": "Registration successful",
                "data": serializer.data
                
                }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "Bad request",
            "message": "Registration unsuccessful",
            "statusCode": 400
            }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            return Response({ 
                "status": "success",
                "message": "Login successful",
                "data": serializer.data
                
                }, status=status.HTTP_200_OK)
        return Response({
            "status": "Bad request",
            "message": "Authentication failed",
            "statusCode": 401
            }, status=status.HTTP_401_UNAUTHORIZED)
    

class GetUserView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        print("USER",request.user)
        print("ID", pk)
        try:
            user = User.objects.get(id=pk)


        except User.DoesNotExist:
            return Response({
            "status": "Bad request",
            "message": "Authentication failed",
            }, status=status.HTTP_401_UNAUTHORIZED)

        serializer = GetUserSerializer(user)
        return Response({ 
                "status": "success",
                "message": "Retrieval successful",
                "data": serializer.data
                
                }, status=status.HTTP_200_OK)

