from rest_framework import serializers
from .models import Ipapp

class IpappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipapp
        fields = '__all__'
