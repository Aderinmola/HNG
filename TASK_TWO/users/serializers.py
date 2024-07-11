from rest_framework import serializers
# from djoser.serializers import UserCreateSerializer

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class AddUserSerializer(serializers.ModelSerializer):
    accessToken = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone', 'accessToken']


    def get_accessToken(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        res = {}
        user = {}
        (instance)
        if instance.id:
            user["userId"] = instance.id
        if instance.first_name:
            user["firstName"] = instance.first_name
        if instance.last_name:
            user["lastName"] = instance.last_name
        if instance.email:
            user["email"] = instance.email
        if instance.phone:
            user["phone"] = instance.phone
        res["accessToken"] = self.get_accessToken(instance)
        res['user'] = user
        return res


class GetUserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone']

    def validate(self, data):
        pass
        # email = data.get('email')
        # password = data.get('password')

        # if email and password:
        #     user = authenticate(
        #         request=self.context.get('request'),
        #         email=email,
        #         password=password
        #     )
        #     if not user:
        #         msg = _('Unable to log in with provided credentials.')
        #         raise serializers.ValidationError(msg, code='authorization')
        # else:
        #     msg = _('Must include "username" and "password".')
        #     raise serializers.ValidationError(msg, code='authorization')

        # return user
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        res = {}
        data = {}
        (instance)
        if instance.id:
            data["userId"] = instance.id
        if instance.first_name:
            data["firstName"] = instance.first_name
        if instance.last_name:
            data["lastName"] = instance.last_name
        if instance.email:
            data["email"] = instance.email
        if instance.phone:
            data["phone"] = instance.phone
        # res['data'] = data
        return data


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)
    accessToken = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone', 'accessToken']

    def get_accessToken(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                email=email,
                password=password
            )
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        # data['user'] = user
        return user
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        res = {}
        user = {}
        (instance)
        if instance.id:
            user["userId"] = instance.id
        if instance.first_name:
            user["firstName"] = instance.first_name
        if instance.last_name:
            user["lastName"] = instance.last_name
        if instance.email:
            user["email"] = instance.email
        if instance.phone:
            user["phone"] = instance.phone
        res["accessToken"] = self.get_accessToken(instance)
        res['user'] = user
        return res

