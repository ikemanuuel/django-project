
from rest_framework import serializers
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password',
                  'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def save(self, **kwargs):
        user = User.objects.create_user(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            password=self.validated_data['password'],

        )
        confirm_password = self.validated_data['confirm_password'],
        user.is_active = False
        user.save()

        return user
