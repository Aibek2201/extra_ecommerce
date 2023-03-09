from rest_framework import serializers
from products import serializers as product_serializers
from . import models


class CreateSellerProductSerializer(serializers.ModelSerializer):
    seller = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Seller_Product
        fields = (
            'seller',
            'product',
            'amount',
            'amount_currency',
            'is_active',
        )


class UpdateSellerProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Seller_Product
        fields = (
            'amount',
            'amount_currency',
            'is_active',
        )


class SellerProductSerializer(serializers.ModelSerializer):
    product = product_serializers.ProductSerializer()

    class Meta:
        model = models.Seller_Product
        fields = '__all__'