

from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, label='Confirm password')

    class Meta:
        model = CustomUser  # Use CustomUser
        fields = ('username', 'email', 'password', 'password2', 'role')  # Include role field

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role='customer'  # Default role for new users
        )
        return user
