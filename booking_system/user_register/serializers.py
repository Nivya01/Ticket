from rest_framework import serializers
from django.contrib.auth import get_user_model
from user_register.models import CustomUser

User = CustomUser

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        if validated_data['user_type'] != 'admin':
            raise serializers.ValidationError("User type must be an admin")
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        if validated_data['user_type'] != 'user':
            raise serializers.ValidationError("User type must be an user")
        user.save()
        return user
    

