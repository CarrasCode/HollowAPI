from typing import override

from rest_framework import serializers

from .models import CustomUser


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
