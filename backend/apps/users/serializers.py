from typing import override

from rest_framework import serializers

from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "password", "confirm_password"]
        extra_kwargs = {"password": {"write_only": True}}

    @override
    def validate(self, attrs):
        if not attrs["password"] == attrs["confirm_password"]:
            raise ValueError("Contraseñas no coinciden")
        return super().validate(attrs)

    @override
    def create(self, validated_data):
        # Extraemos la password para no meterla en texto plano
        validated_data.pop("confirm_password")
        password = validated_data.pop("password")

        return CustomUser.objects.create_user(password=password, **validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "date_joined",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    @override
    def create(self, validated_data):
        # Extraemos la password para no meterla en texto plano
        password = validated_data.pop("password")
        return CustomUser.objects.create_user(password=password, **validated_data)
