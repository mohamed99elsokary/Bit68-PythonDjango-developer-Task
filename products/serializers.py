from rest_framework import serializers
from rest_framework.authtoken.models import Token

from . import models


class CreateProductSerializer(serializers.Serializer):
    # initialize fields

    name = serializers.CharField(write_only=True)
    price = serializers.FloatField(write_only=True)
    seller = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        if validated_data["price"] <= 0:
            raise serializers.ValidationError(
                {"seller": "price must be greater than 0"}
            )
        else:
            try:
                seller = Token.objects.get(key=validated_data["seller"])
                validated_data.pop("seller")
            except:
                raise serializers.ValidationError({"seller": "invalid user Token"})
            product = models.Product.objects.create(
                seller=seller.user, **validated_data
            )
        return product


class ProductSerializer(serializers.Serializer):
    # initialize fields

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.FloatField()
    seller = serializers.CharField()
