from rest_framework import serializers
from .models import Cat
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'user', 'name', 'age', 'breed', 'fur_length')
        read_only_fields = ('user',)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.pop['password'])
        user.save()
        return user