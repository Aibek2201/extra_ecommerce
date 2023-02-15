from rest_framework import serializers
from . import models


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('phone_number', 'email')


class CreateTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class GetUSerSerializer(serializers.Serializer):
    token = serializers.CharField()