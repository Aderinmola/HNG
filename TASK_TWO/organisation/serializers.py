from rest_framework import serializers
from .models import Organisation

class OrganisationSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    class Meta:
        model = Organisation
        fields = ['id', 'name', 'description', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        request = self.context.get('request')
        new_org = super().create(validated_data)
        new_org.user.add(request.user)
        print("USER_ORG", new_org)
        return new_org
        

class SingleOrganisationSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    class Meta:
        model = Organisation
        fields = ['id', 'name', 'description', 'user']
        read_only_fields = ['user']

