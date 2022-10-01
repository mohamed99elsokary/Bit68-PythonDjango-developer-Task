from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class RegisterUserSerializer(serializers.ModelSerializer):
    token = serializers.SlugRelatedField(
        read_only=True, source="auth_token", slug_field="key"
    )

    class Meta:
        model = User
        fields = ["username", "token", "password", "email"]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"write_only": True},
            "email": {"write_only": True},
        }

    def validate(self, data):
        if len(data["password"]) < 8:
            raise serializers.ValidationError(
                {"password": "password must to be more than 7 or more characters"}
            )
        if data.get("email") == "":
            raise serializers.ValidationError({"email": "email can't be empty"})
        if not (data.get("email")):
            raise serializers.ValidationError({"email": "email is required"})
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class LoginUserSerializer(serializers.ModelSerializer):
    token = serializers.SlugRelatedField(
        read_only=True, source="auth_token", slug_field="key"
    )

    class Meta:
        model = User
        fields = ["username", "token", "password", "email"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"write_only": True},
            "username": {"validators": [], "write_only": True},
        }

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user is not None:
            return user
        try:
            user = User.objects.get(username=data["username"])
        except:
            user = None
        if user is None:
            raise serializers.ValidationError({"username": "Invalid username"})
        else:
            raise serializers.ValidationError({"password": "wrong password"})
