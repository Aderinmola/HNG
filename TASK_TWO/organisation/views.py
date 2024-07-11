from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Organisation
from .serializers import OrganisationSerializer, SingleOrganisationSerializer

class OrganisationCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        organisations = Organisation.objects.filter(user=request.user)
        serializer = OrganisationSerializer(organisations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrganisationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleOrganisationView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, format=None):
        print("USER",request.user)
        print("ID", pk)
        try:
            organisation = Organisation.objects.get(id=pk)
        except Organisation.DoesNotExist:
            return Response({
            "status": "Bad request",
            "message": "Organisation does not exist",
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = SingleOrganisationSerializer(organisation)
        return Response({ 
                "status": "success",
                "message": "Retrieval successful",
                "data": serializer.data
                
                }, status=status.HTTP_200_OK)

